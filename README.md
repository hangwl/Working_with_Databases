
# Databases and Data Management

## Database Attributes

In a database management system (DBMS), an attribute refers to a database component, such as a table, record(row), and field(column).

## Keys

**Primary Key**: A primary key serves as a unique identifier for each row in a table and provides a way to quickly and efficiently access specific records. It establishes the primary means of identifying and distinguishing rows in a table. It has the following characteristics:
- primary key values are unique and non-null
- each table can only contain one primary key

**Secondary Key/Unique Key/Alternate Key**: Unique keys are useful when we want to enforce uniqueness on columns that are not designed as the primary key but should have distinct values. E.g. consider a table called "Employees" with columns EmployeeID, EmployeeEmail, and EmployeePhone. While the primary key in this table is the EmployeeID column, we might want to enforce uniqueness on the EmployeeEmail column as well. To achieve this, we can define a unique constraint on the EmployeeEmail column. This ensures that each email address in the table is unique and no two employees can have the same email address.

**Composite**: When creating a table, situations may arise where a single column doesn't provide enough unique information to serve as a primary key. In this case, two columns in the table would be combined to serve as the primary key. E.g. the combination of AuthorID and BookID may qualify as a composite key.

**Foreign Keys**: Foreign keys enable the creation of relationships between two different tables by linking a column in one table to the primary key column in another table. The foreign key constraint ensures that data remains consistent across related tables, maintaining data integrity and enables actions such as cascading updates or deletions.

## Data Redundancy and Data Dependency

**Data Redundancy** refers to the duplication of data within a database system. It occurs when the same piece of data is stored in multiple places or multiple times within the database. Redundancy can arise due to various reasons, such as poor database design or lack of data normalization. Some of the ways data redundancy can negatively impact a database system include:

- Increased storage requirements
- Data inconsistency: data is updated or modified in one place but not in all other instances
- Update anomalies: updating one instance of data may require modifying multiple instances, increasing the risk of inconsistencies

To mitigate data redundancy, database designers often employ techniques such as data normalization, which involves organizing data into well-structured tables and eliminating redundant information. By reducing redundancy, database systems can achieve better data integrity, storage efficiency, and maintainability.

**Data Dependency** refers to the relationship between data elements within a database. It describes how changes or modifications to one piece of data can affect or depend on other related data elements. Understanding data dependencies is crucial for maintaining data integrity and ensuring accurate and consistent results. Two primary types of data dependencies are:

- **Functional Dependency**: occurs when one or more data attributes (columns) in a table determine the values of other attributes. In other words, it describes the relationship between the values of one set of columns and another set of columns in a table. E.g. in a customer table, if the customer id uniquely determines the customer's name, address and phone number, we can say that the customer id functionally determines these attributes, and is represented by CustomerID -> Name, Address, PhoneNumber.
- **Transitive Dependency**: occurs when a functional dependency exists between three or more attributes in a table. It implies that the value of one attribute depends on another attribute, which in turns depends on a third attribute. E.g. consider a product table with attributes such as ProductID, CategoryID, and CategoryName. If CategoryID determines CategoryName, and ProductID determines CategoryID, then we have transitive dependency represented by ProductID -> CategoryID -> CategoryName.

Understanding data dependencies is essential for database design, normalization, and query optimization. By identifying and eliminating unnecessary dependencies, such as transitive dependencies, designers can create more efficient and maintainable database schemas.

## Reducing Data Redundancy to Third Nominal Form (3NF)

3NF is a level of database normalization that helps eliminate redundant data and minimize data anomalies. 3NF builds on 2NF, which builds on 1NF.

- 1NF: requires that each column in a table holds on atomic values, meaning that each value should be indivisible or not further decomposed. Additionally, each column should have a unique name, and there should be a primary key that uniquely identifies each row in the table.
- 2NF: the database must meet the requirements of 1NF and address partial dependencies. A partial dependency exists when a non-key column depends on only a portion of the primary key. To resolve partial dependencies, we need to split the table into two or more separate tables, ensuring that each table has a primary key and contains only columns that are fully dependent on that key.
- 3NF: the database must meet the requirements of 2NF and eliminate transitive dependencies that occur when a non-key column depends on another non-key column, which itself depends on the primary key. This can be done by decomposing the table into multiple tables, ensuring that each non-key column depends only on the primary key and not on any other non-key column.

E.g. consider a table called "Orders" with the following columns: OrderID(PK), CustomerID, CustomerName, CustomerCity. In this case, CustomerName and CustomerCity are dependent on CustomerID, and CustomerID is dependent on OrderID. To achieve 3NF, we can split the table into two separate tables "Orders" (containing OrderID and CustomerId), and "Customers" (containing CustomerID, CustomerName and CustomerCity).

It is important to note that normalization should be done carefully, considering the specific requirements and usage patterns of the database to strike a balance between normalization and performance.

## Entity-Relationship Diagrams

ER Diagrams are visual representations used to model the relationship between entities in a database system. They provide a graphical illustration of the database structure, showing how entities related to each other and the attributes associated with them. Additionally, the serve as a communication tool between database designers, developers, and stakeholders to understand the database schema, entity relationships, and the overall system design. ER diagrams also assist in identifying key elements of the database, such as primary keys, foreign keys, cardinality (the number of occurrences of one entity related to another), and constraints. They provide a high-level overview of the database design and serve as a basis for creating the actual database schema and tables.

[drawio](https://www.drawio.com/) provides a useful diagramming extension integrated into VScode

## NoSQL vs SQL

NoSQL databases are designed to overcome certain limitations of SQL databases and cater to specific use cases. They are well-suited for scenarios involving big data, real-time data, rapid development, scalability, and high-speed data ingestion, such as in social media, IoT applications, and real-time analytics.

PostgreSQL can be considered as a hybrid database that offers a blend of SQL and NoSQL features. It provides developers with the flexibility to work with structured, semi-structured, and unstructured data, making it suitable for a wide range of applications and use cases.

NoSQL features in PostgreSQL include:

- Native JSON and JSONB support: native support for storing, querying, and manipulating JSON data.
- HStore: provides a key-value store within database, which allows for flexible schema-less data storage and retrieval.
- Array Data Type: Arrays can be used to represent collections or lists of values, similar to NoSQL document databases.
- Unstructured Data: through its bytea data type, PostgreSQL supports the storage of unstructured or semi-structured data, such as documents, images, and other binary data.

## Data Privacy and Integrity

Data privacy refers to the protection of sensitive and personally identifiable information (PII) stored within a database. It involves safeguarding data against unauthorized access, misuse, and breaches. Key considerations include:

- Access Control
- Encryption
- Anonymization and Masking
- Compliance with Regulations

Data integrity involves maintaining the accuracy, consistency, and reliability of data throughout its lifecycle within a database. It ensures that data remains unchanged and reliable for users and applications. Key aspects include:

- Data Validation: Implementing data validation checks, such as data type constraints, range checks, and referential integrity constraints, helps ensure that only valid and accurate data is stored in the database.
- Constraints and Rules: Defining integrity constraints, such as primary key constraints, unique constraints, and foreign key constraints, helps enforce data integrity rules and prevent inconsistencies or invalid data relationships.
- Transactional Processing: Employing transactional processing mechanisms, where a set of database operations are treated as a single unit of work, ensures that either all the operations are committed or none are. This helps maintain data integrity during concurrent operations.
- Backup and Recovery: Regularly backing up data and implementing robust disaster recovery mechanisms ensure that data can be restored in the event of data corruption, hardware failures, or other emergencies.
- Audit Trails and Logging: Maintaining audit trails and logs of database activities helps monitor changes, track data modifications, and investigate any potential integrity breaches or unauthorized access attempts.

## Backup vs Archive

Backup refers to the process of creating copies of data or systems to protect against data loss, accidental deletion, hardware failures, or other unforeseen events. The primary purpose of backups is to ensure the ability to restore data to a previous point in time in case of data loss or corruption.

Archiving refers to the process of storing data for long-term preservation, regulatory compliance, historical reference, or business requirements. The primary purpose of archiving is to retain data that is no longer actively used but may still be required for legal, regulatory, or business purposes.

## Version Control and Naming Convention

Version control in database management refers to the practice of managing and tracking changes made to database objects, such as tables, views, stored procedures, or schema definitions, over time. It provides a systematic approach to managing database changes, maintaining a history of modifications, and enabling collaboration among multiple developers. Key aspects of version control in database management include:

- Revision History
- Branching and Merging
- Rollback and Recovery
- Conflict Resolution
- Collaboration and Documentation

Naming conventions in database management refer to the guidelines and standards used for naming database objects such as tables, columns, views, stored procedures, indexes, and other database artifacts. Consistent and meaningful naming conventions enhance clarity, maintainability, and understandability of the database structure. Considerations include: 

- Avoiding reserved words and special characters
- Case sensitivity
- Standardized prefixes or suffixes

## Singapore Personal Data Protection Act (PDPA)

PDPA establishes a framework for organizations to handle personal data responsibly, obtain consent, and provide individuals with control over their data. Compliance with the PDPA is crucial for organizations operating in Singapore to ensure the privacy and security of personal data and avoid potential penalties for non-compliance.