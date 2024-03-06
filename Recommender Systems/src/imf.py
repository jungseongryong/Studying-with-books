from util.models import RecommendResult, Dataset
from src.base_recommender import BaseRecommender
from collections import defaultdict
import numpy as np
import implicit
from scipy.sparse import lil_matrix

np.random.seed(0)


class IMFRecommender(BaseRecommender):
    def recommend(self, dataset: Dataset, **kwargs) -> RecommendResult:
        # 인자 수
        factors = kwargs.get("factors", 10)
        # 평갓값의 임곗값
        minimum_num_rating = kwargs.get("minimum_num_rating", 0)
        # 에폭 수
        n_epochs = kwargs.get("n_epochs", 50)
        # alpha
        alpha = kwargs.get("alpha", 1.0)

        filtered_movielens_train = dataset.train.groupby("movie_id").filter(
            lambda x: len(x["movie_id"]) >= minimum_num_rating
        )

        # 행렬 분석용으로 행렬을 작성한다
        movielens_train_high_rating = filtered_movielens_train[dataset.train.rating >= 4]

        unique_user_ids = sorted(movielens_train_high_rating.user_id.unique())
        unique_movie_ids = sorted(movielens_train_high_rating.movie_id.unique())
        user_id2index = dict(zip(unique_user_ids, range(len(unique_user_ids))))
        movie_id2index = dict(zip(unique_movie_ids, range(len(unique_movie_ids))))

        movielens_matrix = lil_matrix((len(unique_movie_ids), len(unique_user_ids)))
        for i, row in movielens_train_high_rating.iterrows():
            user_index = user_id2index[row["user_id"]]
            movie_index = movie_id2index[row["movie_id"]]
            movielens_matrix[movie_index, user_index] = 1.0 * alpha

        # 모델 초기화
        model = implicit.als.AlternatingLeastSquares(
            factors=factors, iterations=n_epochs, calculate_training_loss=True, random_state=1
        )

        # 학습
        model.fit(movielens_matrix)

        # 추천
        recommendations = model.recommend_all(movielens_matrix.T)
        pred_user2items = defaultdict(list)
        for user_id, user_index in user_id2index.items():
            movie_indexes = recommendations[user_index, :]
            for movie_index in movie_indexes:
                movie_id = unique_movie_ids[movie_index]
                pred_user2items[user_id].append(movie_id)
        # IMF에서는 평갓값의 예측이 어려우므로 rmse 평가는 수행하지 않는다(편의상, 테스트 데이터를 그대로 반환한다).
        return RecommendResult(dataset.test.rating, pred_user2items)


if __name__ == "__main__":
    IMFRecommender().run_sample()
