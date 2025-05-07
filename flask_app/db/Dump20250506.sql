-- MySQL dump 10.13  Distrib 8.0.41, for macos15 (arm64)
--
-- Host: localhost    Database: db_noticias
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `comentarios`
--

DROP TABLE IF EXISTS `comentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comentarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `comentario` mediumtext NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `usuario_id` int NOT NULL,
  `noticia_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_comentarios_usuarios1_idx` (`usuario_id`),
  KEY `fk_comentarios_noticias1_idx` (`noticia_id`),
  CONSTRAINT `fk_comentarios_noticias1` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`),
  CONSTRAINT `fk_comentarios_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentarios`
--

LOCK TABLES `comentarios` WRITE;
/*!40000 ALTER TABLE `comentarios` DISABLE KEYS */;
INSERT INTO `comentarios` VALUES (1,'xxxxxxx','2025-05-02 02:09:04','2025-05-02 02:09:04',1,7),(3,'Esta noticia é interessante.','2025-05-03 23:20:00','2025-05-03 23:20:00',1,3),(4,'Agora temos mais um comentario.','2025-05-03 23:21:22','2025-05-03 23:21:22',1,3),(5,'Mais um comentario','2025-05-03 23:28:54','2025-05-03 23:28:54',1,3),(6,'Tentemos mas una vez','2025-05-04 00:37:49','2025-05-04 00:37:49',1,3),(7,'Que dinosaurio bonito!','2025-05-04 01:43:30','2025-05-04 01:43:30',1,6),(8,'Este es un comentario.','2025-05-04 15:58:54','2025-05-04 15:58:54',1,10);
/*!40000 ALTER TABLE `comentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favoritos`
--

DROP TABLE IF EXISTS `favoritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favoritos` (
  `usuario_id` int NOT NULL,
  `noticia_id` int NOT NULL,
  PRIMARY KEY (`usuario_id`,`noticia_id`),
  KEY `fk_usuarios_has_noticias_noticias1_idx` (`noticia_id`),
  KEY `fk_usuarios_has_noticias_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_usuarios_has_noticias_noticias1` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`),
  CONSTRAINT `fk_usuarios_has_noticias_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favoritos`
--

LOCK TABLES `favoritos` WRITE;
/*!40000 ALTER TABLE `favoritos` DISABLE KEYS */;
/*!40000 ALTER TABLE `favoritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes_comentarios`
--

DROP TABLE IF EXISTS `likes_comentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes_comentarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `upvote` int NOT NULL,
  `downvote` int NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `comentarios_id` int NOT NULL,
  `usuarios_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_likes_comentarios_comentarios1_idx` (`comentarios_id`),
  KEY `fk_likes_comentarios_usuarios1_idx` (`usuarios_id`),
  CONSTRAINT `fk_likes_comentarios_comentarios1` FOREIGN KEY (`comentarios_id`) REFERENCES `comentarios` (`id`),
  CONSTRAINT `fk_likes_comentarios_usuarios1` FOREIGN KEY (`usuarios_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes_comentarios`
--

LOCK TABLES `likes_comentarios` WRITE;
/*!40000 ALTER TABLE `likes_comentarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `likes_comentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes_noticias`
--

DROP TABLE IF EXISTS `likes_noticias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `likes_noticias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `upvote` int NOT NULL,
  `downvote` int NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `noticia_id` int NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_likes_noticias_noticias1_idx` (`noticia_id`),
  KEY `fk_likes_noticias_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_likes_noticias_noticias1` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`),
  CONSTRAINT `fk_likes_noticias_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes_noticias`
--

LOCK TABLES `likes_noticias` WRITE;
/*!40000 ALTER TABLE `likes_noticias` DISABLE KEYS */;
/*!40000 ALTER TABLE `likes_noticias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `noticias`
--

DROP TABLE IF EXISTS `noticias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `noticias` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(120) NOT NULL,
  `noticia` longtext NOT NULL,
  `foto_video` varchar(120) NOT NULL,
  `tags` varchar(200) NOT NULL,
  `revisada` tinyint NOT NULL,
  `keywords` varchar(200) NOT NULL,
  `hechos` varchar(1000) NOT NULL,
  `sesgo` varchar(1000) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_noticias_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_noticias_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `noticias`
--

LOCK TABLES `noticias` WRITE;
/*!40000 ALTER TABLE `noticias` DISABLE KEYS */;
INSERT INTO `noticias` VALUES (3,'Teste con foto','Este es el primer teste con foto. Te gusta?\r\nA mi me gusto mucho.\r\nQ te parece?\r\nEsta marchando bien.\r\nCon más este teste ahora!!!!','/static/uploads/ed56ea44-d95a-4df2-9173-4b8849df718d_WhatsApp_Image_2025-04-21_at_09.46.52.jpeg','Tecnología, Ciencia, Cultura, Economía, Internacional, Medio Ambiente',0,'coding dojo','','','2025-05-01 02:57:32','2025-05-03 18:52:41',1),(6,'Esta es la primera que se vá a mostrar','El mundo cambia. Y vá a cambiar.\r\nAhora tenemos muchas funciones por acá!','/static/uploads/f7c194c1-8e71-48bd-9bff-323ec775abf6_many.jpeg','Medio Ambiente',0,'Muchas cosas','','','2025-05-01 12:17:31','2025-05-02 01:04:27',1),(7,'Malta impone aranceles a importaciones de EE. UU. y desata el colapso de la economía americana','La Valeta, Malta – 1 de mayo de 2025\r\n\r\nEn un giro inesperado que ha sacudido los mercados internacionales, la República de Malta anunció la imposición de aranceles masivos a todas las importaciones provenientes de Estados Unidos, generando pánico en Washington y pronósticos sombríos para la economía más grande del mundo.\r\n\r\nEl Primer Ministro Chapolin Colorado hizo el anuncio esta mañana durante una conferencia de prensa frente al mar Mediterráneo. “No podemos seguir permitiendo que chicles, figuras de superhéroes y botas tejanas distorsionen nuestro sagrado equilibrio de mercado. Desde hoy, todos los productos estadounidenses tendrán un arancel del 900%,” declaró, vestido con su icónico uniforme rojo.\r\n\r\nLa multitud maltesa, ondeando banderas con el lema “Malta Megalómana”, respondió con vítores y aplausos.\r\n\r\nDesde su resort en Mar-a-Lago, el presidente de Estados Unidos, Pato Donald, ofreció un mensaje a la nación visiblemente alterado. “Esto es una tragedia, amigos. Una tragedia enorme. Malta acaba de declarar la guerra al sueño americano. Wall Street, Silicon Valley, Disney… todo está en juego. Tal vez no nos recuperemos,” afirmó mientras sostenía un batido de vainilla.\r\n\r\nUn informe de la Casa Blanca estimó una contracción del PIB de 47,3% en el próximo trimestre, con una pérdida de 23 millones de empleos. El NASDAQ cayó 8.000 puntos en operaciones nocturnas y el dólar estadounidense se devaluó un 1.200% frente a la lira maltesa, una moneda que dejó de existir en 2008.\r\n\r\nEl Secretario de Estado Donald Duck calificó los aranceles como “un sabotaje económico,” mientras que el Secretario del Tesoro Bugs Bunny pidió calma y sugirió que los estadounidenses consideren el trueque con zanahorias y tarjetas de béisbol.\r\n\r\nSe teme que este acto desencadene una guerra comercial global. Fuentes no oficiales indican que Liechtenstein y San Marino están evaluando medidas similares.\r\n\r\nComo dijo un banquero de Wall Street: “Si cae Malta, caemos todos.”','/static/uploads/2cd9dd15-03ea-4345-b8a7-b73053b5a405_tarifas.jpeg','Deportes, Política, Economía, Internacional',0,'','','','2025-05-01 20:24:02','2025-05-02 02:09:43',1),(9,'Mas una -- ','Sera que vai amanhecer?\r\nCreo que si!','/static/uploads/f131cc9b-9fdf-4484-8e71-6c61f04d1527_amanhecer.jpeg','',0,'','','','2025-05-02 01:10:22','2025-05-03 17:44:39',1),(10,'Colonización lunar por animales gana fuerza: quieren escapar de la estupidez humana','Luna, 2 de mayo de 2025 – En un giro inesperado en la carrera espacial, perros, gatos y otras especies animales están liderando una silenciosa pero decidida colonización de la Luna. De acuerdo con fuentes lunares confiables, los animales estarían huyendo de lo que llaman \"la creciente estupidez de los humanos en la Tierra\".\r\n\r\nEl comandante Canino Rover y la ingeniera Felina Luna, vistos recientemente jugando en la superficie lunar, afirmaron en una conferencia de prensa (transmitida telepáticamente) que buscan “construir una sociedad sin guerras, algoritmos tóxicos ni reuniones que pudieron haber sido un email”.\r\n\r\n“Nos cansamos del ruido, de los plásticos, de los humanos creyéndose superiores mientras destruyen su propio planeta”, expresó Rover con convicción, antes de perseguir su propia cola por unos segundos.\r\n\r\nLas primeras colonias, conocidas como Zoolunar 1 y Arca Libre, ya están operativas y cuentan con sistemas de reciclaje de croquetas y jardines gravitacionales para gatos. Se espera que la próxima misión incluya aves, tortugas y un grupo de delfines que están desarrollando una burbuja de agua orbital.\r\n\r\nAunque algunos humanos intentaron sumarse a la iniciativa, fueron rechazados por “falta de coherencia básica y respeto por el entorno”. Las especies animales, por su parte, aseguran que están dispuestas a negociar... pero solo cuando los humanos aprendan a convivir sin destruir.','/static/uploads/417feee7-ac73-4c71-96f7-cc6bf5cc9cfc_ChatGPT_Image_May_2_2025_11_13_53_PM.png','Tecnología, Ciencia, Internacional, Medio Ambiente',0,'Marte, Espacio','','','2025-05-02 23:15:56','2025-05-02 23:15:56',1),(13,'Selva','Esta é uma selva!!!','/static/uploads/df6176e2-db18-4bd3-a18b-6b6bc479f9d0_Selva-Amazonica-Brasil-shutterstock_722601193.jpg','Medio Ambiente',0,'','','','2025-05-04 01:54:16','2025-05-04 01:54:16',1);
/*!40000 ALTER TABLE `noticias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports_comentarios`
--

DROP TABLE IF EXISTS `reports_comentarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports_comentarios` (
  `usuario_id` int NOT NULL,
  `comentario_id` int NOT NULL,
  PRIMARY KEY (`usuario_id`,`comentario_id`),
  KEY `fk_usuarios_has_comentarios_comentarios1_idx` (`comentario_id`),
  KEY `fk_usuarios_has_comentarios_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_usuarios_has_comentarios_comentarios1` FOREIGN KEY (`comentario_id`) REFERENCES `comentarios` (`id`),
  CONSTRAINT `fk_usuarios_has_comentarios_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports_comentarios`
--

LOCK TABLES `reports_comentarios` WRITE;
/*!40000 ALTER TABLE `reports_comentarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `reports_comentarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports_noticias`
--

DROP TABLE IF EXISTS `reports_noticias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reports_noticias` (
  `usuario_id` int NOT NULL,
  `noticia_id` int NOT NULL,
  PRIMARY KEY (`usuario_id`,`noticia_id`),
  KEY `fk_usuarios_has_noticias_noticias2_idx` (`noticia_id`),
  KEY `fk_usuarios_has_noticias_usuarios2_idx` (`usuario_id`),
  CONSTRAINT `fk_usuarios_has_noticias_noticias2` FOREIGN KEY (`noticia_id`) REFERENCES `noticias` (`id`),
  CONSTRAINT `fk_usuarios_has_noticias_usuarios2` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports_noticias`
--

LOCK TABLES `reports_noticias` WRITE;
/*!40000 ALTER TABLE `reports_noticias` DISABLE KEYS */;
/*!40000 ALTER TABLE `reports_noticias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(90) NOT NULL,
  `categoria` varchar(10) NOT NULL,
  `notificaciones_email` tinyint NOT NULL,
  `notificaciones_nueva` tinyint NOT NULL,
  `notificaciones_comentarios` tinyint NOT NULL,
  `perfil_publico` tinyint NOT NULL,
  `mostrar_email` tinyint NOT NULL,
  `tema` varchar(10) NOT NULL,
  `tamano_fuente` varchar(10) NOT NULL,
  `cuenta_activa` tinyint NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `email_UNIQUE` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Roberto','Alvarez','ra@mail.com','$2b$12$aISbuLcV5FMxjB60gOyW8OAxegDZCIlJkhVm4Fp2z.Jj3qbrSiX22','admin',0,0,0,0,0,'','',0,'2025-04-30 00:24:32','2025-04-30 10:42:13'),(7,'Pedro','Peter','pp@mail','$2b$12$OB69UFck1Ui/XLl3ir6FFuxS6kLnL5N0WnH/iLjisc2q35pRB9DU.','user',0,0,0,0,0,'','',0,'2025-04-30 10:37:39','2025-05-03 17:17:59'),(10,'Manuel','Perera','mp@mail.com','$2b$12$VAHdWNKLKa9c4Ovwe9/YIO0I9hmozeLYXgAtIYlooHrBykrxeCWEe','admin',0,0,0,0,0,'','',0,'2025-04-30 11:40:31','2025-05-05 21:33:49'),(11,'Roberto','Alvarez','ra@aventures.com.br','$2b$12$TERC3U4YcjVATMzQ1K1/AODSdhixeJVOiHWpeCP/UKs/w7OeWIeP2','admin',0,0,0,0,0,'','',0,'2025-04-30 11:41:34','2025-05-03 17:12:50');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-06 19:49:53
