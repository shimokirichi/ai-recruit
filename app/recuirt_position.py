from enum import Enum


class RecruitPosition(Enum):

    def __init__(self, id, name_ja, name_en, requirements_responsibilities, requirements_skills):
        self._id = id
        self._name_ja = name_ja
        self._name_en = name_en
        self._requirements_responsibilities = requirements_responsibilities
        self._requirements_skills = requirements_skills

    @property
    def id(self):
        return self._id

    @property
    def name_ja(self):
        return self._name_ja

    @property
    def name_en(self):
        return self._name_en

    @property
    def requirements_responsibilities(self):
        return self._requirements_responsibilities

    @property
    def requirements_skills(self):
        return self._requirements_skills

    ENGINNEER = (
        1,
        "engineer",
        "エンジニア",
        """
            1. Write, test, and fix code for our applications using React.js.
            2. Collaborate with the team, syncing code regularly using tools like Git.
            3. Create reusable components for future projects, using tools like Bit or Storybook.
        """,
        """
            1.Strong skills in JavaScript, CSS, HTML, and other frontend languages.
            2. Proficient in React.js, Webpack, and Enzyme.
            3. Troubleshooting skills with tools like React DevTools and Chrome Developer Tools.
            4. Good communication skills for technical and non-technical discussions.
        """
    )
    SALE_MAN = (
        2,
        "sale man",
        "営業員",
        """
            1. Reach out to potential clients using tools like LinkedIn Sales Navigator.
            2. Conduct market research with tools like Google Analytics and SEMrush.
            3. Generate reports with data and visualizations for actionable insights.
            4. Manage client relationships using CRM tools like Salesforce or HubSpot.
            5. Understand customer needs through surveys and sentiment analysis tools.

        """,
        """
            1. Proven sales experience, preferable 3+years in any industry
            2. Familiarity with quantitative tools for market trend analysis.
            3. Strong interpersonal skills and a customer-focused approach.
            4. Proficient in data visualization tools like Tableau or Power BI.
            5. Clear verbal and written communication skills.

        """
    )
