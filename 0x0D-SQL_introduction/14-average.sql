-- computes the score average of all records in the table second_table.

ALTER TABLE second_table ADD average DECIMAL(5, 4);
SELECT AVG(score) as average FROM second_table;
