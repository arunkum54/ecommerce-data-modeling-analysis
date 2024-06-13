-- sql_queries.sql

-- Query 1: Retrieve the top 5 customers who have made the highest average order amounts in the last 6 months
SELECT customer_id, AVG(total_amount) as average_order_amount
FROM Orders
WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY customer_id
ORDER BY average_order_amount DESC
LIMIT 5;

-- Query 2: Retrieve the list of customers whose order value is lower this year compared to previous year
WITH yearly_orders AS (
    SELECT customer_id, YEAR(order_date) as order_year, SUM(total_amount) as yearly_total
    FROM Orders
    GROUP BY customer_id, YEAR(order_date)
)
SELECT this_year.customer_id
FROM yearly_orders this_year
JOIN yearly_orders last_year
ON this_year.customer_id = last_year.customer_id
AND this_year.order_year = YEAR(CURDATE())
AND last_year.order_year = YEAR(CURDATE()) - 1
WHERE this_year.yearly_total < last_year.yearly_total;

-- Query 3: Create a table showing cumulative purchase by a particular customer, with a breakdown by product category
SELECT c.customer_id, c.name, p.category, SUM(od.quantity * od.unit_price) as cumulative_purchase
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Details od ON o.order_id = od.order_id
JOIN Product_Variants pv ON od.variant_id = pv.variant_id
JOIN Products p ON pv.product_id = p.product_id
GROUP BY c.customer_id, c.name, p.category;

-- Query 4: Retrieve the list of top 5 selling products, bifurcated by product variants
SELECT p.product_name, pv.variant_name, SUM(od.quantity) as total_quantity
FROM Products p
JOIN Product_Variants pv ON p.product_id = pv.product_id
JOIN Order_Details od ON pv.variant_id = od.variant_id
GROUP BY p.product_name, pv.variant_name
ORDER BY total_quantity DESC
LIMIT 5;
