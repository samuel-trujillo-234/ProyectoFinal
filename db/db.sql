-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_noticias
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_noticias
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_noticias` DEFAULT CHARACTER SET utf8 ;
USE `db_noticias` ;

-- -----------------------------------------------------
-- Table `db_noticias`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_noticias`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `email` VARCHAR(60) NOT NULL,
  `password` VARCHAR(90) NOT NULL,
  `categoria` VARCHAR(10) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_noticias`.`noticias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_noticias`.`noticias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(120) NOT NULL,
  `noticia` LONGTEXT NOT NULL,
  `foto_video` VARCHAR(120) NOT NULL,
  `tags` JSON NOT NULL,
  `revisada` TINYINT NOT NULL,
  `keywords` JSON NOT NULL,
  `hechos` JSON NOT NULL,
  `sesgo` JSON NOT NULL,
  `created_at` DATETIME NOT NULL,
  `upodated_at` DATETIME NOT NULL,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_noticias_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_noticias_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_noticias`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_noticias`.`comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_noticias`.`comentarios` (
  `id` INT NOT NULL,
  `titulo` VARCHAR(90) NOT NULL,
  `comentario` MEDIUMTEXT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `usuario_id` INT NOT NULL,
  `noticia_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comentarios_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  INDEX `fk_comentarios_noticias1_idx` (`noticia_id` ASC) VISIBLE,
  CONSTRAINT `fk_comentarios_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_noticias`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comentarios_noticias1`
    FOREIGN KEY (`noticia_id`)
    REFERENCES `db_noticias`.`noticias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_noticias`.`likes_noticias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_noticias`.`likes_noticias` (
  `id` INT NOT NULL,
  `upvote` INT NOT NULL,
  `downvote` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `noticia_id` INT NOT NULL,
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_likes_noticias_noticias1_idx` (`noticia_id` ASC) VISIBLE,
  INDEX `fk_likes_noticias_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_noticias_noticias1`
    FOREIGN KEY (`noticia_id`)
    REFERENCES `db_noticias`.`noticias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_noticias_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_noticias`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_noticias`.`likes_comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_noticias`.`likes_comentarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `upvote` INT NOT NULL,
  `downvote` INT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `comentarios_id` INT NOT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_likes_comentarios_comentarios1_idx` (`comentarios_id` ASC) VISIBLE,
  INDEX `fk_likes_comentarios_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_comentarios_comentarios1`
    FOREIGN KEY (`comentarios_id`)
    REFERENCES `db_noticias`.`comentarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_comentarios_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `db_noticias`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_noticias`.`preferidas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_noticias`.`preferidas` (
  `usuario_id` INT NOT NULL,
  `noticia_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `noticia_id`),
  INDEX `fk_usuarios_has_noticias_noticias1_idx` (`noticia_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_noticias_usuarios1_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_noticias_usuarios1`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `db_noticias`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_noticias_noticias1`
    FOREIGN KEY (`noticia_id`)
    REFERENCES `db_noticias`.`noticias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_noticias`.`denuncias_noticias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_noticias`.`denuncias_noticias` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `explicacion` MEDIUMTEXT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `noticias_id` INT NOT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_denuncias_noticias1_idx` (`noticias_id` ASC) VISIBLE,
  INDEX `fk_denuncias_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_denuncias_noticias1`
    FOREIGN KEY (`noticias_id`)
    REFERENCES `db_noticias`.`noticias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_denuncias_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `db_noticias`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_noticias`.`denuncias_comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_noticias`.`denuncias_comentarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `explicacion` MEDIUMTEXT NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `usuarios_id` INT NOT NULL,
  `comentarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_denuncias_comentarios_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  INDEX `fk_denuncias_comentarios_comentarios1_idx` (`comentarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_denuncias_comentarios_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `db_noticias`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_denuncias_comentarios_comentarios1`
    FOREIGN KEY (`comentarios_id`)
    REFERENCES `db_noticias`.`comentarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
