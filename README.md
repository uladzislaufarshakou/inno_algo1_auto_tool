# Python LLM Learning Authomatization Tool

## 📝 Plan of Work

### This is a high-level overview of the project development plan.

### More detailed specifications will be added for each phase as work progresses.

1.  **Data Ingestion**: Create a class to fetch data from repository files and load it into a PostgreSQL database.
2.  **Question Retrieval**: Implement a Google Sheets agent to monitor for and retrieve unprocessed questions.
3.  **LLM Integration**: Develop a Google Gemini agent to connect to the Gemini API and process the retrieved questions.
4.  **Query Execution**: Build a class to execute the Gemini-generated SQL queries against the target Snowflake database and other ones if needed.

### Now working on: Data Ingestion

# TODO:

- [x] Create a todo list for the current phase of development

- [ ] Create an interface IDatabase (as a Strategy interface)
- [ ] Create at least a PostgresDB (as a concrete Strategy realization)

- [ ] Create an interface IReader (as a Strategy interface)
- [ ] Create a JsonlReader (as a concrete Strategy realization)
- [ ] Create a CsvReader (as a concrete Strategy realization)

- [ ] Create class Processor which will connect
      all previously described classes together

- [ ] Setup settings.py via pydantic_settings

Plan can (and probably will) be modified while working on it
