CREATE TABLE `carts` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) NOT NULL COMMENT '使用者_id',
  `product_id` bigint(20) NOT NULL COMMENT '產品_id',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '創見時間',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;