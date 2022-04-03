CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_bin NOT NULL COMMENT '用户名',
  `password` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '密碼',
  `phone` varchar(20) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '手機號碼',
  `email` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL COMMENT '信箱',
  `create_time` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '創見時間',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

INSERT INTO `test`.`users` (`id`, `username`, `password`, `phone`, `email`, `create_time`) VALUES ('1', 'xiao', '123', '0912345678', 'apple@qq.com', '2020-04-10 01:22:07');
INSERT INTO `test`.`users` (`id`, `username`, `password`, `phone`, `email`, `create_time`) VALUES ('2', 'fnong', '543', '0923456781', 'banana@qq.com', '2020-04-11 02:24:25');
INSERT INTO `test`.`users` (`id`, `username`, `password`, `phone`, `email`, `create_time`) VALUES ('3', 'chone', '981', '0934567812', 'orange@qq.com', '2020-04-12 13:07:49');
INSERT INTO `test`.`users` (`id`, `username`, `password`, `phone`, `email`, `create_time`) VALUES ('4', 'bob', '746', '0945678123', 'lemon@qq.com', '2020-04-12 18:31:16');
INSERT INTO `test`.`users` (`id`, `username`, `password`, `phone`, `email`, `create_time`) VALUES ('5', 'sana', '342', '0956781234', 'tomato@qq.com', '2020-04-13 07:44:23');
INSERT INTO `test`.`users` (`id`, `username`, `password`, `phone`, `email`, `create_time`) VALUES ('6', 'elegan', '582', '0967812345', 'pieapple@qq.com', '2020-04-14 21:32:24');