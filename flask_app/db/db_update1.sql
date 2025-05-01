-- MySQL Workbench Synchronization
-- Generated: 2025-05-01 00:03
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Roberto Alvarez

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER SCHEMA `db_noticias`  DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci ;

ALTER TABLE `db_noticias`.`noticias` 
DROP FOREIGN KEY `fk_noticias_usuarios1`;

ALTER TABLE `db_noticias`.`comentarios` 
DROP FOREIGN KEY `fk_comentarios_noticias1`;

ALTER TABLE `db_noticias`.`likes_noticias` 
DROP FOREIGN KEY `fk_likes_noticias_noticias1`,
DROP FOREIGN KEY `fk_likes_noticias_usuarios1`;

ALTER TABLE `db_noticias`.`likes_comentarios` 
DROP FOREIGN KEY `fk_likes_comentarios_comentarios1`,
DROP FOREIGN KEY `fk_likes_comentarios_usuarios1`;

ALTER TABLE `db_noticias`.`preferidas` 
DROP FOREIGN KEY `fk_usuarios_has_noticias_noticias1`;

ALTER TABLE `db_noticias`.`denuncias_noticias` 
DROP FOREIGN KEY `fk_denuncias_noticias1`,
DROP FOREIGN KEY `fk_denuncias_usuarios1`;

ALTER TABLE `db_noticias`.`denuncias_comentarios` 
DROP FOREIGN KEY `fk_denuncias_comentarios_comentarios1`;

ALTER TABLE `db_noticias`.`usuarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ,
ADD COLUMN `notificaciones_email` TINYINT(4) NOT NULL AFTER `categoria`,
ADD COLUMN `notificaciones_nueva` TINYINT(4) NOT NULL AFTER `notificaciones_email`,
ADD COLUMN `notificaciones_comentarios` TINYINT(4) NOT NULL AFTER `notificaciones_nueva`,
ADD COLUMN `perfil_publico` TINYINT(4) NOT NULL AFTER `notificaciones_comentarios`,
ADD COLUMN `mostrar_email` TINYINT(4) NOT NULL AFTER `perfil_publico`,
ADD COLUMN `tema` VARCHAR(10) NOT NULL AFTER `mostrar_email`,
ADD COLUMN `tamano_fuente` VARCHAR(10) NOT NULL AFTER `tema`,
ADD COLUMN `cuenta_activa` TINYINT(4) NOT NULL AFTER `tamano_fuente`;

ALTER TABLE `db_noticias`.`noticias` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`comentarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`likes_noticias` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`likes_comentarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`preferidas` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`denuncias_noticias` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`denuncias_comentarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`noticias` 
ADD CONSTRAINT `fk_noticias_usuarios1`
  FOREIGN KEY (`usuario_id`)
  REFERENCES `db_noticias`.`usuarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `db_noticias`.`comentarios` 
DROP FOREIGN KEY `fk_comentarios_usuarios1`;

ALTER TABLE `db_noticias`.`comentarios` ADD CONSTRAINT `fk_comentarios_usuarios1`
  FOREIGN KEY (`usuario_id`)
  REFERENCES `db_noticias`.`usuarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_comentarios_noticias1`
  FOREIGN KEY (`noticia_id`)
  REFERENCES `db_noticias`.`noticias` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `db_noticias`.`likes_noticias` 
ADD CONSTRAINT `fk_likes_noticias_noticias1`
  FOREIGN KEY (`noticia_id`)
  REFERENCES `db_noticias`.`noticias` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_likes_noticias_usuarios1`
  FOREIGN KEY (`usuario_id`)
  REFERENCES `db_noticias`.`usuarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `db_noticias`.`likes_comentarios` 
ADD CONSTRAINT `fk_likes_comentarios_comentarios1`
  FOREIGN KEY (`comentarios_id`)
  REFERENCES `db_noticias`.`comentarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_likes_comentarios_usuarios1`
  FOREIGN KEY (`usuarios_id`)
  REFERENCES `db_noticias`.`usuarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `db_noticias`.`preferidas` 
DROP FOREIGN KEY `fk_usuarios_has_noticias_usuarios1`;

ALTER TABLE `db_noticias`.`preferidas` ADD CONSTRAINT `fk_usuarios_has_noticias_usuarios1`
  FOREIGN KEY (`usuario_id`)
  REFERENCES `db_noticias`.`usuarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_usuarios_has_noticias_noticias1`
  FOREIGN KEY (`noticia_id`)
  REFERENCES `db_noticias`.`noticias` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `db_noticias`.`denuncias_noticias` 
ADD CONSTRAINT `fk_denuncias_noticias1`
  FOREIGN KEY (`noticias_id`)
  REFERENCES `db_noticias`.`noticias` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_denuncias_usuarios1`
  FOREIGN KEY (`usuarios_id`)
  REFERENCES `db_noticias`.`usuarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;

ALTER TABLE `db_noticias`.`denuncias_comentarios` 
DROP FOREIGN KEY `fk_denuncias_comentarios_usuarios1`;

ALTER TABLE `db_noticias`.`denuncias_comentarios` ADD CONSTRAINT `fk_denuncias_comentarios_usuarios1`
  FOREIGN KEY (`usuarios_id`)
  REFERENCES `db_noticias`.`usuarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_denuncias_comentarios_comentarios1`
  FOREIGN KEY (`comentarios_id`)
  REFERENCES `db_noticias`.`comentarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
