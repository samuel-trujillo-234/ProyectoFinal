-- MySQL Workbench Synchronization
-- Generated: 2025-05-04 16:28
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

ALTER TABLE `db_noticias`.`favoritos` 
DROP FOREIGN KEY `fk_usuarios_has_noticias_noticias1`;

ALTER TABLE `db_noticias`.`usuarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`noticias` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`comentarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`likes_noticias` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`likes_comentarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `db_noticias`.`favoritos` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

CREATE TABLE IF NOT EXISTS `db_noticias`.`reports_noticias` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `noticias_id` INT(11) NOT NULL,
  `usuario_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_denuncias_noticias1_idx` (`noticias_id` ASC) VISIBLE,
  INDEX `fk_denuncias_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_denuncias_noticias1`
    FOREIGN KEY (`noticias_id`)
    REFERENCES `db_noticias`.`noticias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_denuncias_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_noticias`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `db_noticias`.`reports_comentarios` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `usuario_id` INT(11) NOT NULL,
  `comentario_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_denuncias_comentarios_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  INDEX `fk_denuncias_comentarios_comentarios1_idx` (`comentario_id` ASC) VISIBLE,
  CONSTRAINT `fk_denuncias_comentarios_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_noticias`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_denuncias_comentarios_comentarios1`
    FOREIGN KEY (`comentario_id`)
    REFERENCES `db_noticias`.`comentarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

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

ALTER TABLE `db_noticias`.`favoritos` 
DROP FOREIGN KEY `fk_usuarios_has_noticias_usuarios1`;

ALTER TABLE `db_noticias`.`favoritos` ADD CONSTRAINT `fk_usuarios_has_noticias_usuarios1`
  FOREIGN KEY (`usuario_id`)
  REFERENCES `db_noticias`.`usuarios` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION,
ADD CONSTRAINT `fk_usuarios_has_noticias_noticias1`
  FOREIGN KEY (`noticia_id`)
  REFERENCES `db_noticias`.`noticias` (`id`)
  ON DELETE NO ACTION
  ON UPDATE NO ACTION;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
