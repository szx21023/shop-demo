CREATE TABLE `products` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '產品名',
  `stars` integer NOT NULL COMMENT '推薦星星數',
  `price` integer NOT NULL COMMENT '價錢',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '創見時間',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `test`.`products` (`id`, `name`, `stars`, `price`, `create_time`) VALUES ('1', 'apple', '3', '123', '2020-04-10 01:22:07');
INSERT INTO `test`.`products` (`id`, `name`, `stars`, `price`, `create_time`) VALUES ('2', 'banana', '4', '543', '2020-04-11 02:24:25');
INSERT INTO `test`.`products` (`id`, `name`, `stars`, `price`, `create_time`) VALUES ('3', 'pieapple', '1', '981', '2020-04-12 13:07:49');
INSERT INTO `test`.`products` (`id`, `name`, `stars`, `price`, `create_time`) VALUES ('4', 'orange', '5', '746', '2020-04-12 18:31:16');
INSERT INTO `test`.`products` (`id`, `name`, `stars`, `price`, `create_time`) VALUES ('5', 'watermelon', '4', '342', '2020-04-13 07:44:23');
INSERT INTO `test`.`products` (`id`, `name`, `stars`, `price`, `create_time`) VALUES ('6', 'lemon', '3', '582', '2020-04-14 21:32:24');