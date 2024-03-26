# Movies Chatbot
Chatbot with knowledge database - [Wikipedia Movie Plots datasets from Kaggle](https://www.kaggle.com/datasets/jrobischon/wikipedia-movie-plots), using LangChain, FAISS Vector Database and LLM.

To run locally:
1. Clone repository
2. Create virtual environment
3. Activate the environment
4. Install requirements
```
pip install -r requirements.txt
```
5. Download dataset from Kaggle (link above) and place in data folder
6. Run ingest_data.py script to calculate embeddings of the texts from dataset and store them in a vector database.
```
python ingest_data.py
```
7. Run chatbot.py to start a simple gradio GUI and interact with a model.
```
python chatbot.py.py
```
8. Ask the chatbot about your favourite movie!
