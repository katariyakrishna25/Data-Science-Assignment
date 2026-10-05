-- SESSION 2 - Database Setup + CREATE TABLE


-- QUESTION 1
-- Verify MySQL installation and connection.
-- Run these commands in MySQL.

SELECT VERSION();

SELECT DATABASE();


-- QUESTION 2
-- Create the foodie_app database.

CREATE DATABASE foodie_app;

USE foodie_app;


-- QUESTION 3
-- Create the restaurants table.

CREATE TABLE restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine VARCHAR(50),
    rating DECIMAL(2,1),
    location VARCHAR(100)
);


-- QUESTION 4
-- Create the users table for a Flipkart-style app.

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    username VARCHAR(50) UNIQUE,
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15) UNIQUE,
    created_at DATETIME
);


-- QUESTION 5
-- Intentionally incorrect CREATE TABLE statement.
-- Missing comma after cuisine column.

CREATE TABLE test_restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine VARCHAR(50)
    rating DECIMAL(2,1),
    location VARCHAR(100)
);


-- Corrected CREATE TABLE statement.

CREATE TABLE test_restaurant (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine VARCHAR(50),
    rating DECIMAL(2,1),
    location VARCHAR(100)
);