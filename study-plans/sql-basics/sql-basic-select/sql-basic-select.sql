-- Returns: name, category, inventory_value.
SELECT product_name AS name, category, unit_price * units_in_stock as inventory_value from products;