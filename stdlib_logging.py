import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv())
