from langchain import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="intfloat/e5-large-v2", model_kwargs={"device": "cuda"})
vector_db = FAISS.load_local("vector_db_faiss", embedding_model, allow_dangerous_deserialization=True)


def similarity_search(query: str):
    q_embedding = embedding_model.embed_documents([query])[0]
    relevant_doc = vector_db.similarity_search_by_vector(q_embedding, k=3)
    return relevant_doc


if __name__ == '__main__':
    docs1 = similarity_search("Tony Stark")
    print(docs1[0])
    print("")
    print(docs1[1])
    print("")
    print(docs1[2])
    print("")