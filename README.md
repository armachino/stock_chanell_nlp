
# 🧠 Telegram Financial Sentiment Analyzer

This Python application scrapes Telegram messages from finance-related groups and channels (Stock, Crypto, and Forex), performs sentiment analysis using a custom-trained model, and outputs buy/sell sentiment for financial instruments. It is intended to run **once daily**, not in real-time.

---

## 📦 Project Structure

```
.
├── core/
│   ├── constants.py            # Constants used across the project
│   ├── infrences.py            # Sentiment analysis and inference logic
│   ├── main.py                 # Entry point to run the scraper and sentiment analysis
│   ├── models/                 # Contains trained models
│   │   └── stock_nlp_model_v1.pickle  # Trained model for stock sentiment analysis
│   ├── openai_api.py           # OpenAI API integration for text embeddings
│   ├── preprocess_chats.py     # Chat preprocessing logic
│   ├── __pycache__/            # Compiled Python files
│   ├── stocks/                 # Stock-related data
│   │   └── stocks_tsetmcs.csv  # Example stock data
│   ├── telegram_api.py         # Telegram API integration for chat scraping
│   └── utils/                  # Utility functions
│       ├── __init__.py         # Initialization for utils module
│       ├── text.py             # Text processing utilities
│       └── __pycache__/        # Compiled Python files for utils
├── embeded_chats.csv           # Scraped and embedded chat data
├── environment.yml             # Conda environment file with dependencies
├── play_ground/                # Directory for experimentation and model training
│   ├── keyword.json            # Keyword file used for analysis
│   ├── lab/                    # Training and testing notebooks
│   │   ├── create_model.ipynb  # Jupyter notebook for model creation
│   │   ├── data/               # Raw and processed chat data for training
│   │   │   ├── chats/          # Raw chat data files
│   │   │   │   ├── boursgram.json
│   │   │   │   ├── gp_bazar.json
│   │   │   │   └── result.json
│   │   │   ├── chats_17may/    # Raw chat data for a specific period
│   │   │   │   ├── boursgram.json
│   │   │   │   ├── golden.json
│   │   │   │   ├── gp_bazar.json
│   │   │   │   └── majid.json
│   │   │   ├── concatenated2.csv  # Concatenated data for analysis
│   │   │   ├── concatenated.csv   # Another concatenated dataset
│   │   │   └── labeled_dataset.json # Labeled dataset used for training
│   │   ├── digikala/            # Digikala-related notebooks and data
│   │   │   ├── Digikala_sentiment_analysis.ipynb  # Sentiment analysis notebook
│   │   │   └── test.ipynb        # Additional test notebook
│   │   ├── Route_1.ipynb         # Experimentation notebook 1
│   │   ├── Route_2.ipynb         # Experimentation notebook 2
│   │   ├── stock_nlp_model_v1.pickle # Trained model for sentiment analysis
│   │   ├── stock.session         # Session data used for model training
│   │   └── telegrammmm.xlsx      # Excel file with additional Telegram data
│   └── stocks/                  # Stock-related scraping data
│       ├── scrapper.js           # JavaScript scraper for stocks data
│       └── stocks_tsetmcs.csv    # Stocks data
├── pred_chats.csv               # Predictions made by the model
├── preprocessed_chats.csv       # Preprocessed chat data
├── README.md                    # Project documentation
```

---

## 🔍 Features

- ✅ Scrapes Telegram groups/channels related to **stocks**, **cryptocurrencies**, and **forex**
- ✅ Embeds messages using **OpenAI embeddings API**
- ✅ Trained custom sentiment analysis model using:
  - Hand-labeled messages (by a domain specialist)
  - AI-labeled data (via ChatGPT)
- ✅ Returns structured insights with a **sentiment label (positive/negative)** for each asset
- ✅ Runs **daily**, not designed for real-time monitoring

---

## ⚙️ How It Works

1. **Data Collection**:
   - Connects to Telegram via the **Telethon** API
   - Scrapes new messages from specified groups and channels related to stock, crypto, and forex

2. **Text Embedding**:
   - Uses OpenAI's `text-embedding-ada-002` API to convert scraped messages into vector form

3. **Inference**:
   - Loads a custom-trained sentiment analysis model from `core/models/stock_nlp_model_v1.pickle`
   - Predicts whether a message suggests a **positive or negative sentiment** for a financial asset
   - Extracts asset names (e.g., stock tickers, crypto coins, forex pairs) mentioned in the message

4. **Output**:
   - Saves the results to **pred_chats.csv** with asset names, sentiments, and message details

---

## 🧪 Training Details

- **Labeling Process**:
  - A small portion of the data was labeled manually by a finance expert
  - The remaining data was labeled using ChatGPT-based heuristics and manually verified
- **Model**:
  - Sentiment analysis model trained using the labeled dataset located in `play_ground/lab/`
  - The trained model is saved in `core/models/stock_nlp_model_v1.pickle`

---

## 🚀 Getting Started

### Prerequisites

- **Conda**: Install Conda if you don’t have it.
- **Telegram API credentials** (`api_id`, `api_hash`)
- **OpenAI API key**

### Installation

Clone the repository and create a Conda environment:

```bash
git clone https://github.com/yourusername/stock_chanell_nlp.git
cd stock_chanell_nlp
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate stock_chanell_nlp
```

### Configuration

Create a `.env` file or update the `config/` folder with the following credentials:

```ini
# OpenAi
OPENAI_API_KEY=your_openai_key
# Telegram
Telegram_API_ID=your_telegram_api_id
Telegram_API_HASH=your_telegram_api_hash
```

### Run the App

```bash
python core/main.py
```

---

## 📅 Schedule Daily Run (Optional)

To run the script daily, set up a cron job or use a scheduler like **Airflow**:

Example `cron` (Linux):

```cron
python core/main.py
```

---

## 🧠 Future Improvements

- Add a web dashboard to visualize insights
- Improve asset name extraction using advanced NLP techniques
- Fine-tune the model with more labeled datasets from additional Telegram channels
- Enable multi-language support (for non-English groups)

---

<!-- ## 📄 License

MIT License. See [LICENSE](LICENSE) for details. -->
