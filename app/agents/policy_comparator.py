from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class PolicyComparator:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2') # free local model

        def compare_policies(self, policy_texts):
            #Embed policy texts
            embeddings = self.model.encode(policy_texts)

            # Calculate similarity matrix
            similarity_matrix = cosine_similarity(embeddings)

            # Find most similar pair
            most_similar = np.unravel_index(
                np.argmax(similarity_matrix - np.eye(len(policy_texts))),
                similarity_matrix.shape
            )

            # Find most defferent pair
            most_different = np.unravel_index(
                np.argmin(similarity_matrix + np.eye(len(policy_texts)) * 10),
            )

            return {
                'similarity_matrix': similarity_matrix,
                'most_similar': most_similar,
                'most_different': most_different,
                'average_similarity': np.mean(similarity_matrix)
            }