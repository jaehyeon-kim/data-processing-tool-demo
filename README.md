# data-processing-tool-demo

Demo data processing tool

[![data-processing-tool](https://github.com/jaehyeon-kim/data-processing-tool-demo/actions/workflows/main.yml/badge.svg)](https://github.com/jaehyeon-kim/data-processing-tool-demo/actions/workflows/main.yml)

## Examples

```bash
./cli.py list
# Available functions: mean, median, sum

./cli.py  process --filepath ./ext/input.csv --group_by_col first_name --apply_col count --func_name mean
# Processing csv file: ./ext/input.csv, group by first_name, apply on count, function mean
# first_name
# john       11.0
# kristen    17.0
# piers      10.0
# sam        15.0
# Name: count, dtype: float64

./cli.py  process --filepath ./ext/nba-2017.csv --group_by_col TEAM --apply_col SALARY_MILLIONS --func_name mean
# Processing csv file: ./ext/nba-2017.csv, group by TEAM, apply on SALARY_MILLIONS, function mean
# TEAM
# ATL         6.830000
# ATL/CLE     5.240000
# BKN         5.094286
# BKN/WSH     6.090000
# BOS         6.768182
# CHA        10.041667
# CHI         7.143000
# CHI/OKC     4.850000
# CLE        18.582000
# CLE/DAL     0.910000
# DAL        12.493333
# DAL/BKN     1.790000
# DAL/PHI     2.945000
# DEN         5.235455
# DEN/POR     1.920000
# DET         5.405000
# GS         13.855000
# GS/CHA      1.470000
# HOU        12.105000
# HOU/LAL     4.670000
# HOU/MEM     1.580000
# IND         7.098571
# LAC        12.031667
# LAL         8.303333
# MEM        10.178000
# MIA         5.497143
# MIL         7.587143
# MIL/CHA     9.425000
# MIN         5.140000
# NO          9.071667
# NO/ORL      0.060000
# NO/SAC      8.970000
# NY         11.971429
# NY/PHI      1.310000
# OKC         8.318750
# ORL         8.737143
# ORL/TOR    10.000000
# PHI         6.958000
# PHX         7.307143
# POR        12.550000
# SA         11.835714
# SAC         5.173333
# TOR         6.507500
# UTAH        6.525000
# WSH        11.525714
# Name: SALARY_MILLIONS, dtype: float64
```
