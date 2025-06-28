import sqlite3


conn = sqlite3.connect('policies.db')
cursor = conn.cursor()


cursor.execute("DROP TABLE IF EXISTS policies")


cursor.execute('''
CREATE TABLE policies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    type TEXT,
    age_group TEXT,
    income_group TEXT,
    coverage TEXT,
    description TEXT
)
''')


policies = [
    ('Health Secure', 'Health', '18-40', 'middle', '5L', 'Affordable health policy for young adults.'),
    ('Senior Shield', 'Health', '60+', 'middle', '10L', 'Comprehensive health insurance for senior citizens.'),
    ('Term Life Plus', 'Life', '25-50', 'high', '1Cr', 'Term life insurance with high coverage.'),
    ('Child Future Plan', 'Education', '30-45', 'middle', '20L', 'Helps secure your child’s education needs.'),
    ('Saver Invest', 'Investment', '25-40', 'middle', 'Flexible', 'A mix of saving and investment with returns.'),
    ('Elite Life Cover', 'Life', '30-60', 'high', '2Cr', 'Premium life cover with long-term savings benefits.'),
    ('Health Gold', 'Health', '18-55', 'high', '15L', 'Cashless hospitalization with global coverage.'),
    ('Pension Secure', 'Retirement', '45-60', 'middle', '30L', 'Plan for your retirement with steady returns.'),
    ('Women’s Wellness Plan', 'Health', '25-45', 'middle', '8L', 'Specially curated plan for women’s health needs.'),
    ('Family Floater', 'Health', '25-50', 'middle', '10L', 'One plan covering all family members.'),
    ('Smart Child Plan', 'Education', '25-40', 'low', '10L', 'Low-premium policy for future child education.'),
    ('Wealth Builder', 'Investment', '30-50', 'high', 'Flexible', 'High-return ULIP plan with tax benefits.'),
    ('Micro Health Cover', 'Health', '18-40', 'low', '2L', 'Minimal premium policy for essential health needs.'),
    ('Term Secure Lite', 'Life', '25-45', 'low', '50L', 'Affordable term life cover for starters.'),
    ('Senior Income Plan', 'Retirement', '60+', 'middle', '20L', 'Monthly income and health support post retirement.'),
    ('EduPlus Guardian', 'Education', '30-50', 'middle', '15L', 'Combines education savings with life cover.'),
    ('Critical Care Cover', 'Health', '40-65', 'high', '20L', 'Covers major critical illnesses like cancer, heart attack.'),
    ('Super Saver Plan', 'Investment', '20-40', 'low', 'Flexible', 'Low-risk investment with long-term gain.'),
    ('Whole Life Income', 'Life', '30-60', 'middle', '1Cr', 'Guaranteed income + whole life insurance.'),
    ('Travel Protect', 'Travel', '18-60', 'middle', '5L', 'Covers international travel emergencies and baggage loss.')
]


cursor.executemany('''
INSERT INTO policies (name, type, age_group, income_group, coverage, description)
VALUES (?, ?, ?, ?, ?, ?)
''', policies)


conn.commit()
conn.close()

print("✅ Database 'policies.db' initialized and populated with 20 policies.")
