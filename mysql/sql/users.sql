CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '用户名',
  `password` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '密碼',
  `phone` varchar(20) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '手機號碼',
  `email` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '信箱',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '創見時間',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `test`.`users` (`id`, `username`, `password`, `phone`, `email`, `create_time`) VALUES ('1', 'xiao', '123', '12345678910', '123@qq.com', '2020-04-10 01:22:07');
INSERT INTO `test`.`users` (`id`, `username`, `password`, `phone`, `email`, `create_time`) VALUES ('2', 'fnong', '543', '87654321', '123@qq.com', '2020-04-11 02:24:25');