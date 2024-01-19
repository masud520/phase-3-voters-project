# phase-3-voters-project

This project is a simple demonstration of a voter management system using SQLAlchemy, a popular SQL toolkit and Object-Relational Mapping (ORM) library for Python.

## Overview

The project defines three main entities: Author, Category, and Quote. It also includes a join table QuoteCategory to establish a many-to-many relationship between quotes and categories.

### Entities

   - Attributes: id (Primary Key), 
   - Relationship: One-to-Many with
   - Attributes: id (Primary Key), 
   - Relationship: Many-to-Many with.
   - Attributes: id (Primary Key), text, author_id (Foreign Key).
   - Relationships: Many-to-One with Author, Many-to-Many with Category.
   - Represents the many-to-many relationship between Quote and Category.
   - Attributes: id (Primary Key),  (Foreign Key), category_id (Foreign Key).


## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/masud520/phase-3-voters-project

    Navigate to the project directory:

    bash

cd phase-3-voters-project

**Install the required dependencies:**

bash

**pip install -r requirements.txt**

Run the application:

bash

**python your_main_script.py**

**##Dependencies**

    SQLAlchemy: A SQL toolkit and Object-Relational Mapping (ORM) library for Python.

**###AUTHOR**
MASUD ABDI
###**LICENCE**
MIT
