**Installation & Setup**
1. Clone Repository & Setup Environment
bash
git clone <repo_link>
cd product_management
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.\.venv\Scripts\activate   # Windows


**2. Install Dependencies**
bash
pip install -r requirements.txt

**3. Configure .env File (if using environment variables)**
env
SECRET_KEY=your_django_secret_key
DEBUG=True
DB_NAME=product_db
DB_USER=postgres
DB_PASSWORD=mitali@123
DB_HOST=localhost
DB_PORT=5432
CELERY_BROKER_URL=redis://localhost:6379/0
**
4. Apply Migrations**
bash
python manage.py makemigrations
python manage.py migrate

**5. Run the Server**
bash
python manage.py runserver

6. Start Redis & Celery Workers
bash
redis-server  # Start Redis
celery -A product_management worker --loglevel=info  # Start Celery Worker
**API Endpoints**

Authentication
Method	Endpoint	Description
POST	/auth/register/	Register a user
POST	/auth/login/	Login and get token
POST	/auth/logout/	Logout & blacklist token


**Category Management**
Method	Endpoint	Description
POST	/categories/	Create category (Admin Only)
GET	/categories/	List all categories
GET	/categories/{id}/	Get specific category
PATCH	/categories/{id}/	Update category (Admin Only)
DELETE	/categories/{id}/	Soft delete category (Admin Only)


**Product Management**
Method	Endpoint	Description
POST	/products/	Create product (Admin Only)
GET	/products/	List all products
GET	/products/{id}/	Get specific product
PATCH	/products/{id}/	Update product (Admin Only)
DELETE	/products/{id}/	Soft delete product (Admin Only)


**Bulk Upload**
Method	Endpoint	Description
POST	/upload/	Upload JSON file for bulk data
