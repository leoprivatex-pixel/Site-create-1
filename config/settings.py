import os

class Settings:

    # Project
    PROJECT_NAME = "proxy-ai-platform"

    PROJECT_PATH = "./site"

    # Skills
    SKILLS_PATH = "./skills"

    ENABLE_SKILLS = True

    # Agents
    MAX_AGENTS = 12

    ENABLE_AUTO_REFACTOR = True
    ENABLE_AUTO_DEBUG = True

    # Development loop
    MAX_DEV_ITERATIONS = 100

    # Proxy system
    PROXY_ROTATION_ENABLED = True

    PROXY_ROTATION_STRATEGY = "round_robin"

    PROXY_HEALTH_CHECK = True

    # Decodo integration
    DECODO_API_URL = "https://api.decodo.com"

    DECODO_API_KEY = os.getenv("DECODO_API_KEY")

    # Billing
    BILLING_ENABLED = True

    PAYMENT_PROVIDER = "stripe"

    # Database
    DATABASE_URL = "sqlite:///proxy_platform.db"

    # Logging
    LOG_LEVEL = "INFO"

    LOG_FILE = "logs/system.log"

    # Security
    ENABLE_RATE_LIMIT = True

    ENABLE_AUTH = True

settings = Settings()