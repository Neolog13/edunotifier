from celery import Celery

def create_celery_app():
    """Создание и настройка Celery app"""
    app = Celery('edunotifier')

    app.conf.update(
        broker_url='redis://localhost:6379/0',
        result_backend='redis://localhost:6379/0',
        task_serializer='json',
        accept_content=['json'],
        result_serializer='json',
        timezone='Europe/Moscow',
        enable_utc=True,
        
        # Настройки для логирования только в терминал
        worker_log_format='[%(asctime)s: %(levelname)s/%(processName)s] %(message)s',
        worker_task_log_format='[%(asctime)s: %(levelname)s/%(processName)s] %(message)s',
        worker_redirect_stdouts=True,
        worker_redirect_stdouts_level='INFO',
    )

    return app
