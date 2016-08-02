# matify
Quick script to convert CSV files with text fields to numeric fields and produce associated legend.

Octave and MATLAB don't play well with CSV files with text fields. This script simply converts string columns to numeric ones. It does a single pass of all text typed columns and figures out all the unique values for that column and assigns each unique value an index. It then replaces each member of that column with its associated index.
