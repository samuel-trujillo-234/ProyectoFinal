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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comentarios`
--

LOCK TABLES `comentarios` WRITE;
/*!40000 ALTER TABLE `comentarios` DISABLE KEYS */;
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
  `tipo` varchar(10) NOT NULL,
  `analisis` varchar(500) NOT NULL,
  `sesgo` json NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  KEY `fk_noticias_usuarios1_idx` (`usuario_id`),
  CONSTRAINT `fk_noticias_usuarios1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `noticias`
--

LOCK TABLES `noticias` WRITE;
/*!40000 ALTER TABLE `noticias` DISABLE KEYS */;
INSERT INTO `noticias` VALUES (33,'Colonización lunar por animales gana fuerza: quieren escapar de la estupidez humana','\r\nLuna, 2 de mayo de 2025 – En un giro inesperado en la carrera espacial, perros, gatos y otras especies animales están liderando una silenciosa pero decidida colonización de la Luna. De acuerdo con fuentes lunares confiables, los animales estarían huyendo de lo que llaman \"la creciente estupidez de los humanos en la Tierra\".\r\n \r\n El comandante Canino Rover y la ingeniera Felina Luna, vistos recientemente jugando en la superficie lunar, afirmaron en una conferencia de prensa (transmitida telepáticamente) que buscan “construir una sociedad sin guerras, algoritmos tóxicos ni reuniones que pudieron haber sido un email”.\r\n \r\n “Nos cansamos del ruido, de los plásticos, de los humanos creyéndose superiores mientras destruyen su propio planeta”, expresó Rover con convicción, antes de perseguir su propia cola por unos segundos.\r\n \r\n Las primeras colonias, conocidas como Zoolunar 1 y Arca Libre, ya están operativas y cuentan con sistemas de reciclaje de croquetas y jardines gravitacionales para gatos. Se espera que la próxima misión incluya aves, tortugas y un grupo de delfines que están desarrollando una burbuja de agua orbital.\r\n \r\n Aunque algunos humanos intentaron sumarse a la iniciativa, fueron rechazados por “falta de coherencia básica y respeto por el entorno”. Las especies animales, por su parte, aseguran que están dispuestas a negociar... pero solo cuando los humanos aprendan a convivir sin destruir.','/static/uploads/f8cb081f-f69b-49d4-bacd-2195918e5668_animales.png','Tecnología, Ciencia, Internacional, Medio Ambiente',0,'','-1','El texto no representa un artículo de noticias objetivo, sino más bien parece una obra de ficción o un artículo de opinión. Esto se basa en el contenido del artículo que incluye detalles imaginativos improbables, como animales que lideran una colonización de la luna y animales llevando a cabo conferencias de prensa telepáticas.','{\"summary\": \"La narrativa del autor critica fuertemente la acción humana en la Tierra y apoya la iniciativa de los animales de colonizar la luna para vivir en armonía y proteger el medio ambiente. Esta visión critica aspectos de la economía humana, subraya la necesidad de respeto y conservación cultural y rechaza las posturas establecidas de las élites humanas.\", \"cultural\": {\"label\": \"progresista\", \"score\": -0.7, \"features\": [\"la creciente estupidez de los humanos en la Tierra\", \"escapando de los humanos creyéndose superiores\", \"respeto por el entorno\"], \"confidence\": 1}, \"economic\": {\"label\": \"leve-izquierda\", \"score\": -0.2, \"features\": [\"sociedad sin guerras\", \"algoritmos tóxicos\", \"reuniones que pudieron haber sido un email\", \"reciclaje de croquetas\", \"jardines gravitacionales\"], \"confidence\": 0.8}, \"institutional\": {\"label\": \"fuertemente anti-élite\", \"score\": -0.9, \"features\": [\"falta de coherencia básica\", \"humanos aprendan a convivir sin destruir\"], \"confidence\": 0.85}}','2025-05-08 20:13:02','2025-05-08 20:13:16',1),(43,'Cenário Digital Brasil','O cenário da publicidade digital no Brasil, que movimenta quase R$ 38 bilhões anualmente e cresceu 60% nos últimos quatro anos, impõe desafios crescentes a anunciantes e agências, como destacou o diretor de estratégias digitais do Correio Braziliense, Luiz Mendes. Longe de ser um ambiente simples, a era digital exige estratégias mais sofisticadas e um olhar atento não apenas para a tecnologia, mas para o fator humano e a garantia da entrega. Essa foi a tônica do evento CB Talks — O Futuro Digital, uma parceria entre o Correio e a Realize. O encontro reuniu especialistas do setor para analisar o atual momento da publicidade digital e apontar as perspectivas para o segmento.','/static/uploads/dbaa36ab-01ca-43eb-bdb8-8a91ca1c50a5_ambiente-digital.jpg','',0,'','1','El texto presenta información sobre el estado actual de la publicidad digital en Brasil, informa cifras económicas y menciona a especialistas y su opinión profesional. No se identifica ninguna opinión personal del autor ni se promueven ideas subjetivas, por lo tanto, se puede clasificar como un artículo de noticias objetivo basado en datos.','{\"summary\": \"El autor ofrece una visión muy neutra y directa sobre la publicidad digital en Brasil y cómo está creciendo a pasos agigantados. No hay ninguna indicación clara de cuál es la postura ideológica del autor, pero dada la discusión sobre las exigencias sofisticadas que la era digital impone a anunciantes y agencias, se podría inferir un ligero sesgo hacia la derecha en los ejes económicos y culturales. Sin embargo, la confianza en este sesgo es baja debido a la falta de pruebas sólidas.\", \"cultural\": {\"label\": \"centro-derecha\", \"score\": 0.1, \"features\": [], \"confidence\": 0.5}, \"economic\": {\"label\": \"centro-derecha\", \"score\": 0.1, \"features\": [], \"confidence\": 0.5}, \"institutional\": {\"label\": \"neutro\", \"score\": 0, \"features\": [], \"confidence\": 1}}','2025-05-12 00:54:09','2025-05-12 00:54:22',1),(45,'Presidente Lula se reune com empresários chineses nesta segunda-feira','O presidente da República, Luiz Inácio Lula da Silva, se reunirá com empresários em Pequim nesta segunda-feira (12/5). Segundo o Palácio do Planalto, o presidente se reunirá com os diretores executivos de duas grandes empresas chinesas. Lula segue em visita oficial à China pelos próximos dias.\r\nO primeiro encontro será com Lei Zhang, CEO da Envision Energy, produtora de turbinas eólicas, e a depois será com Cheng Fubo, CEO da Norinco, uma corporação industrial que atua em setores como defesa, automotivo, fabricação de máquinas, produtos químicos, eletrônicos.\r\nAs reuniões serão realizadas no hotel em que Lula está hospedado ao longo da manhã de segunda-feira (no horário da China). Pela tarde, o presidente se reúne com empresários da saúde e assinará acordos. Por fim, Lula marcará presença no encerramento do seminário Brasil-China, evento que reune empresários brasileiros e chineses.\r\nNa terça-feira (13/4), a agenda oficial continua com Lula participando da cúpula de chefes de Estado e de Governo da Comunidade de Estados Latino-americanos e Caribenhos (Celac) com o governo da China. Então, se encontrar com demais autoridades chinesas, como o presidente da Comissão Permanente da Assembleia Nacional Popular, Zhao Leji, e o primeiro-ministro da China, Li Qiang.\r\nE no fim da terça, Lula e o presidente da China, Xi Jinping, se reunirão no Palácio do povo. É esperado que, pelo menos, 16 acordos sejam assinados entre Brasil e China nesse encontro.','/static/uploads/8e75a90e-8cee-48d2-a1ca-3ca6105e78b2_LulaChina.png','Tecnología, Política, Ciencia, Economía, Salud, Internacional',0,'','1','El texto proporciona hechos y eventos de la agenda oficial del presidente de Brasil, sin agregar interpretaciones o juicios personales. Tal y como se detalla en el itinerario y las personas con las que se reunirá, este es claramente un reportaje objetivo basado en hechos.','{\"summary\": \"Este texto presenta una perspectiva neutral a moderadamente progresista y levemente anti-elitista. No se observan elementos significativos que resalten un sesgo económico. El sesgo cultural es ligeramente progresista, demostrado por la participación en la Comunidad de Estados Latino-americanos y Caribeños. El sesgo institucional es levemente anti-elitista, reflejado en las reuniones con figuras empresariales y del gobierno chino.\", \"cultural\": {\"label\": \"Levemente progresista\", \"score\": -0.2, \"features\": [\"Participación en la Comunidad de Estados Latino-americanos y Caribeños\"], \"confidence\": 0.65}, \"economic\": {\"label\": \"neutral\", \"score\": 0, \"features\": [], \"confidence\": 0.9}, \"institutional\": {\"label\": \"Levemente anti-elitista\", \"score\": -0.1, \"features\": [\"Reunión con directores ejecutivos de empresas chinas\", \"Reunión con empresarios de la salud\"], \"confidence\": 0.75}}','2025-05-12 01:08:00','2025-05-12 01:08:12',1),(46,'SBA under Trump','WASHINGTON, DC — Small Business Administration (SBA) Administrator Kelly Loeffler told Breitbart News that the legislation she announced with lawmakers this week would help bring back American “economic independence” and supercharge the return of American industry by boosting SBA loans to small businesses.\r\n\r\nAdministrator Loeffler, Senate Small Business Committee Chair Joni Ernst (R-IA), House Small Business Committee Chairman Roger Williams, and Sen. Chris Coons (D-DE) make headlines this week when they announced the Made in America Manufacturing Finance Act, a bill that seeks to boost manufacturing in the United States by boosting the capital available to small businesses through the SBA.\r\nSpecifically, the bill, if passed through Congress, would double the individual loan limit for the 7(a) and 504 small manufacturing loans from $5 million to $10 million.\r\n\r\nLoeffler sees the legislation as something everyone can get behind regardless of political affiliation.\r\n“It was really exciting to be able to in the first 100 days, to be able to work on a piece of bipartisan legislation. And, I think there’s nothing more bipartisan than small businesses, they power our local communities and innovation,” the Small Business Administration leader said.\r\n\r\nLoeffler said that the increased access to capital would help American entrenepeuers and build more in the Unites States.\r\n“I’ve been out on the road, whether it’s talking with our lenders, great thing about the SBA, It’s a public private partnership. The costs are really not borne by the taxpayer. The local lenders are the ones making the loans provide a guarantee that is self funding. But we’ve heard both from lenders and our manufacturers, of which 99 percent qualify as small businesses, that they need more capital. These these loan limits at $5 million were set years, decades ago, and obviously with inflation and the sophistication of automation, manufacturing, we need to have more resources to access to capital.”\r\n\r\nShe continued, noting that the increased capital through these SBA loans would complement the Trump tax cuts.\r\n“That’s going to allow them to hire, expand and invest much more quickly, particularly as President Trump’s tax cuts are made permanent. I really think manufacturing is spring loaded. If we can get those tax cuts passed quickly, you will see a strong trajectory of growth in the manufacturing sector and well beyond,” she explained.\r\n\r\nThe SBA is blazing the trail to encourage beneficial lending for the Trump economy in a fashion that many other government bodies and even corporations could embrace.\r\n\r\nBreitbart News economics editor John Carny wrote in November 2024 that these loans could be used to help create the “new Trump economy.”\r\n“Many of these pro-growth reforms can begin even without congressional action. Only the additional tax cuts would require new laws to take effect. But each of them could be strengthened if Congress later enshrined the changes into law, guaranteeing that the next administration could not undo them with the stroke of a pen,” Carney wrote.\r\n\r\nLoeffler said that the potential is there to make things across Main Streets across America.\r\n\r\nShe said she has talked to “a lot of governors and their economic development teams. The conversations are happening right now in real time, and that is thanks to President Trump’s Liberation Day, which freed us from being completely dependent on the Chinese Communist Party and return that to Main Street, to Peoria, to Pittsburgh, and Little Rock, and every place in between that we need to make things in this country, and that is actually happening. And so I think it would be hard for someone to stand in the way of that type of legislation.”\r\nLoeffler said that the SBA does not merely provide capital to small businesses; the agency also provides guidance, including how to reshore or onshore manufacturing in the United States.\r\n\r\nShe explained, “Part of our role is providing access to capital, but another part of our role is counseling, making sure that we’re providing the connection, so that when a manufacturer is trying to onshore or expand their supply chain access in the United States, we’re providing that information. So we’re also working on connecting small businesses with local manufacturers. We’ll be rolling out more of those concepts in the near term.”\r\n\r\nLoeffler continued, “I think the biggest thing with access to capital means that that manufacturer, who’s maybe kind of the smallish manufacturer that is being relied on aerospace or automotive or other things that we’re seeing emergency emerging around technology semiconductors, that they’re going to be able to say, ‘Okay, I can commit to that contract with that larger manufacturer. I can subcontract now, because I can buy that equipment, machinery and make the hires I need to do.\r\nShe said that the president’s policies would help bring back growth and economic independence, which will revitalize Americans nationwide.\r\n\r\nLoeffler said that the president’s policies are “bringing back our economic independence and progress. Prosperity. We’re not going to be dependent on the Chinese Communist Party. We’re becoming energy dominant. Again, I love that. That’s absolutely strategically critical around the world. But we’re really elevating Main Streets. We’re making sure that our communities, rural communities, urban communities, people aren’t left behind.”','/static/uploads/a3997a80-f6bc-47f5-aba2-28e7150e0a07_sba.jpeg','Política, Economía, Internacional',0,'','0.6','El texto parece ser en su mayoría un reporte objetivo de generalidades en torno a una ley propuesta y comentarios de la Administradora de la Administración de Pequeños Negocios, Kelly Loeffler. Sin embargo, hay cierto sesgo evidente en la forma en que se presentan las políticas de Trump y las opiniones positivas de Loeffler sobre estas políticas se citan sin crítica. Además, se cita a Breitbart News, un medio conocido por su inclinación conservadora.','{\"summary\": \"El autor parece apoyar firmemente las políticas económicas pro-empresariales y las reducciones de impuestos impulsadas por el presidente Trump y su administración. Destaca la iniciativa de la SBA para fomentar préstamos beneficiosos para las pequeñas empresas y elogia la legislación que busca incrementar la independencia económica de los EE.UU. En general, el narrador muestra un sesgo de derecha, progreso conservador y pro-establishment en su análisis de las políticas actuales.\", \"cultural\": {\"label\": \"conservador moderado\", \"score\": 0.5, \"features\": [\"brexit news economics editor John Carny wrote in November 2024 that these loans could be used to help create the “new Trump economy\", \"the president’s policies would help bring back growth and economic independence\"], \"confidence\": 0.6}, \"economic\": {\"label\": \"derecha\", \"score\": 0.8, \"features\": [\"legislation she announced with lawmakers this week would help bring back American “economic independence”\", \"boosting SBA loans to small businesses\", \"the bill, if passed through Congress, would double the individual loan limit\", \"Loeffler sees the legislation as something everyone can get behind regardless of political affiliation\", \"the increased capital through these SBA loans would complement the Trump tax cuts\", \"the president’s policies are “bringing back our economic independence and progress\"], \"confidence\": 0.9}, \"institutional\": {\"label\": \"pro-establishment\", \"score\": 0.7, \"features\": [\"Loeffler, Senate Small Business Committee Chair Joni Ernst (R-IA), House Small Business Committee Chairman Roger Williams\", \"the increased capital through these SBA loans would complement the Trump tax cuts\", \"The SBA is blazing the trail to encourage beneficial lending for the Trump economy\", \"Loeffler said that the president’s policies are “bringing back our economic independence and progress\"], \"confidence\": 0.88}}','2025-05-12 01:33:01','2025-05-12 01:33:19',1),(49,'Malta impone aranceles a importaciones de EE. UU. y desata el colapso de la economía americana','La Valeta, Malta – 1 de mayo de 2025\r\n\r\nEn un giro inesperado que ha sacudido los mercados internacionales, la República de Malta anunció la imposición de aranceles masivos a todas las importaciones provenientes de Estados Unidos, generando pánico en Washington y pronósticos sombríos para la economía más grande del mundo.\r\n \r\n El Primer Ministro Chapolin Colorado hizo el anuncio esta mañana durante una conferencia de prensa frente al mar Mediterráneo. “No podemos seguir permitiendo que chicles, figuras de superhéroes y botas tejanas distorsionen nuestro sagrado equilibrio de mercado. Desde hoy, todos los productos estadounidenses tendrán un arancel del 900%,” declaró, vestido con su icónico uniforme rojo.\r\n \r\n La multitud maltesa, ondeando banderas con el lema “Malta Megalómana”, respondió con vítores y aplausos.\r\n \r\n Desde su resort en Mar-a-Lago, el presidente de Estados Unidos, Pato Donald, ofreció un mensaje a la nación visiblemente alterado. “Esto es una tragedia, amigos. Una tragedia enorme. Malta acaba de declarar la guerra al sueño americano. Wall Street, Silicon Valley, Disney… todo está en juego. Tal vez no nos recuperemos,” afirmó mientras sostenía un batido de vainilla.\r\n \r\n Un informe de la Casa Blanca estimó una contracción del PIB de 47,3% en el próximo trimestre, con una pérdida de 23 millones de empleos. El NASDAQ cayó 8.000 puntos en operaciones nocturnas y el dólar estadounidense se devaluó un 1.200% frente a la lira maltesa, una moneda que dejó de existir en 2008.\r\n \r\n El Secretario de Estado Donald Duck calificó los aranceles como “un sabotaje económico,” mientras que el Secretario del Tesoro Bugs Bunny pidió calma y sugirió que los estadounidenses consideren el trueque con zanahorias y tarjetas de béisbol.\r\n \r\n Se teme que este acto desencadene una guerra comercial global. Fuentes no oficiales indican que Liechtenstein y San Marino están evaluando medidas similares.\r\n \r\n Como dijo un banquero de Wall Street: “Si cae Malta, caemos todos.”','/static/uploads/41b19b28-0e09-4215-915f-1dbc2fe9c422_hafenbild-valletta--malta-.jpg','Economía, Internacional',0,'','-0.4','El texto parece ser un informe de noticias debido a su formato y estilo, pero incluye características indistinguibles de la sátira o la ficción exagerada. Las referencias a personajes de caricaturas en roles políticos importantes y afirmaciones extremas sobre el impacto económico de los aranceles sugieren que no es completamente un informe de noticias basado en datos objetivos. Sin embargo, no se trata puramente de una opinión ya que no parece estar promoviendo una perspectiva personal.','{\"summary\": \"El autor presenta un relato fuertemente crítico hacia las políticas económicas estadounidenses y parece aprobar la decisión de Malta de imponer fuertes aranceles. La narrativa se inclina hacia la izquierda en términos económicos y muestra un claro sesgo anti-establecimiento. A pesar de que las descripciones son irónicas y parodias a figuras conocidas, el autor parece alentar un cambio en el equilibrio de poder económico.\", \"cultural\": {\"label\": \"Centro-Izquierda\", \"score\": -0.2, \"features\": [\"“No podemos seguir permitiendo que chicles, figuras de superhéroes y botas tejanas distorsionen nuestro sagrado equilibrio de mercado.\", \"“Malta acaba de declarar la guerra al sueño americano.\", \"“Si cae Malta, caemos todos.”\"], \"confidence\": 0.65}, \"economic\": {\"label\": \"Izquierda-Centro\", \"score\": -0.6, \"features\": [\"No podemos seguir permitiendo que chicles, figuras de superhéroes y botas tejanas distorsionen nuestro sagrado equilibrio de mercado.\", \"Desde hoy, todos los productos estadounidenses tendrán un arancel del 900%,”\"], \"confidence\": 0.8}, \"institutional\": {\"label\": \"Anti-Establecimiento\", \"score\": -0.8, \"features\": [\"En un giro inesperado que ha sacudido los mercados internacionales, la República de Malta anunció la imposición de aranceles masivos a todas las importaciones provenientes de Estados Unidos.\", \"El primer ministro, Chapolin Colorado, hizo el anuncio esta mañana.\", \"Se teme que este acto desencadene una guerra comercial global.\"], \"confidence\": 0.9}}','2025-05-12 01:47:57','2025-05-12 01:48:15',1),(51,'Trump shares America','\r\nThe government under President Donald Trump is bending the arc of US history in a new direction, away from the civil rights focus of the past 60 plus years.\r\n\r\nAddressing or even acknowledging racial injustice toward people of color is out.\r\n\r\nSeparating church and state is out, according to Trump.\r\n\r\nExposing anti-Christian bias and being ‘anti-woke’ is in.\r\n\r\nThe Department of Justice division created by the landmark 1957 Civil Rights Act to defend American’s rights has a new mission: rooting out anti-Christian bias, antisemitism and “woke ideology,” the head of the division, Harmeet Dhillon, recently told conservative commentator Glenn Beck.\r\n\r\nA majority of the lawyers at the Civil Rights division – people who got jobs there to ensure equal access to the ballot box, perhaps – are expected to resign with pay until September.\r\n\r\nAt a White House Cabinet meeting Wednesday, secretaries repeatedly sought praise from Trump for purging diversity efforts from the government.\r\n\r\n“We’re not organizing money based on the color of skin,” said Agriculture Secretary Brooke Rollins, referring to contracts cancelled at USDA.\r\n\r\n“If you’re having DEI policies, we’re not going to fund your projects,” said Transportation Secretary Sean Duffy, bragging about how the administration will use taxpayer dollars to kill diversity efforts in states.\r\n\r\nOffice of Management and Budget Director Russell Vought told Trump the administration had forgiven money a Chicago lender paid as part of a discrimination settlement.\r\n\r\n“We’ve ripped wokeness out of the military, sir, DEI, trans. And it’s Fort Benning and Fort Bragg again at the DOD,” said Defense Secretary Pete Hegseth, referring to bases that again share names with Confederate generals.\r\n\r\nThe administration is also working to strong-arm elite universities into dropping DEI programs by threatening billions in funding, including for scientific research. Harvard, so far, has decided to fight back.\r\n\r\nBut there are other examples, such as the fact that while the US has stopped accepting refugees for the most part, it is accepting White South Africans who claim they are the victims of racism in their country.\r\n\r\nNot since Reconstruction\r\nIt’s a much larger pivot than simply changing hiring practices and stopping so-called DEI efforts.\r\n\r\n“This is certainly the biggest rollback of civil rights since Reconstruction,” according to Mark Updegrove, a presidential historian and CEO of the LBJ Foundation.\r\n\r\nTrump’s policies and the way he’s orienting his government combine as an assault on the Great Society legislation Johnson pushed through in the 1960s, including the Voting Rights Act, the Civil Rights Act of 1964 and the Immigration and Nationality Act of 1965.\r\nComparing Trump’s effort to purge the country of diversity efforts and deconstruct the Great Society legislation, Updegrove drew a parallel between now and the period beginning during Reconstruction when post-Civil War advances like the 13th Amendment were hurt by the rise of White Supremacy and Jim Crow.\r\n\r\n“We’re seeing something very similar now, rolling back the advances of the 1960s,” he said. While those Great Society laws were meant to be temporary measures to create a more equal society, Updegrove said the US is not yet there. “So called anti-wokeism,” he argued, is “essentially permission to accept racism.”\r\n\r\nCuts to Medicaid spending, higher education programs like Pell Grants, or Head Start programs would also hurt efforts at making the US a more equitable society.\r\n\r\n“If you ultimately look at what Trump is doing, it is aimed at taking down the laws of the Great Society, which are effectively, in my view, the foundation of modern America and the path to a plural democracy for the first time in our history.”\r\n\r\nRetreat from civil rights and a push into religious freedom\r\nWhile Trump’s government is retreating from any effort by the federal government to pursue racial justice, it is leaning hard into ending what it sees as anti-Christian bias.\r\n\r\nA task force helmed by Attorney General Pam Bondi and focused on “eradicating” anti-Christian bias in the government held its first meeting this week.\r\n\r\nAt the majority-Catholic Supreme Court, justices were re-evaluating the separation of church and state this week. Conservative justices seemed open during oral arguments to the idea of taxpayer dollars going to fund a Catholic charter school in Oklahoma. The conservative Justice Amy Coney Barrett recused herself from the arguments, leaving the outcome likely up to Chief Justice John Roberts.\r\n\r\nThe Solicitor General of the United States, D. John Sauer, who previously represented Trump before the court, argued on behalf of the Catholic charter school.\r\n\r\n“We’re bringing religion back to our country,” Trump promised at a prayer breakfast in Washington on Thursday, where he said he will also sign a new executive order to create another commission, this one focused on religious liberty.\r\n\r\nTrump seemed to acknowledge that some people might be surprised to hear that there is bias against Christians in a country that is majority Christian.\r\n\r\n“You haven’t heard that, but there’s anti-Christian bias, also,” he said.\r\n\r\nEven many Christians say it does not exist in the widespread way it is being portrayed by Trump’s administration.\r\n\r\n“When he discusses anti-Christian bias, he isn’t referring to Christianity at large or mainstream Christianity, which includes Episcopalians, Catholics, Lutherans, Quakers, and even the LDS Church,” said Rev. Paul Brandeis Raushenbush of the Interfaith Alliance during an appearance on CNN after the announcement of the commission to eradicate anti-Christian bias.\r\n\r\nBrandeis is among those who worry of a slide away from the freedom of religion envisioned at the nation’s founding and toward a Christian nationalism.\r\n\r\n“This White House exploits faith for power, following a Christian nationalist playbook,” he said.','/static/uploads/eafaa6fb-1a98-4ae6-9159-0f0fa5ec2fe7_trumpeloni.jpeg','Política, Economía, Internacional',1,'','-1','El texto presenta una fuerte carga de opinión en su enfoque y lenguaje. Maneja inferencias y deducciones acerca de las políticas y acciones del gobierno de Donald Trump y sugiere intenciones y objetivos sin basarse en declaraciones o políticas documentadas y confirmadas por fuentes oficiales. Además, emplea lenguaje emotivo y juicios de valor, característicos de los artículos de opinión.','{\"summary\": \"El autor del artículo presenta un enfoque narrativo fuertemente crítico hacia la administración de Trump, enfatizando las políticas y acciones que percibe como regresivas en términos de derechos civiles y diversidad. El tono y lenguaje sugieren un desacuerdo con la orientación política y cultural que Trump está implementando. Notablemente, el autor destaca los esfuerzos de la administración para reducir la diversidad, avanzar en los derechos cristianos en detrimento de la separación de iglesia y estado, y retroceder en políticas económicas destinadas a reducir la desigualdad.\", \"cultural\": {\"label\": \"conservador\", \"score\": 0.9, \"features\": [\"Separating church and state is out, according to Trump\", \"Exposing anti-Christian bias and being ‘anti-woke’ is in\", \"it is accepting White South Africans who claim they are the victims of racism in their country\"], \"confidence\": 0.9}, \"economic\": {\"label\": \"derecha\", \"score\": 0.7, \"features\": [\"Trump’s policies\", \"If you’re having DEI policies, we’re not going to fund your projects\", \"Cuts to Medicaid spending, higher education programs like Pell Grants, or Head Start programs\"], \"confidence\": 0.8}, \"institutional\": {\"label\": \"pro-establecimiento\", \"score\": 0.6, \"features\": [\"The Department of Justice division created by the landmark 1957 Civil Rights Act to defend American’s rights has a new mission: rooting out anti-Christian bias, antisemitism and “woke ideology,\", \"“We’re bringing religion back to our country,” Trump promised\", \"The conservative Justice Amy Coney Barrett recused herself from the arguments, leaving the outcome likely up to Chief Justice John Roberts\"], \"confidence\": 0.85}}','2025-05-12 01:55:42','2025-05-12 01:55:58',1);
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
  `notificaciones_nuevas` tinyint NOT NULL,
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
INSERT INTO `usuarios` VALUES (1,'Roberto','Alvarez','ra@mail.com','$2b$12$aISbuLcV5FMxjB60gOyW8OAxegDZCIlJkhVm4Fp2z.Jj3qbrSiX22','admin',0,0,0,0,0,'','',0,'2025-04-30 00:24:32','2025-04-30 10:42:13'),(7,'Pedro','Peter','pp@mail','$2b$12$OB69UFck1Ui/XLl3ir6FFuxS6kLnL5N0WnH/iLjisc2q35pRB9DU.','user',0,0,0,0,0,'','',0,'2025-04-30 10:37:39','2025-05-03 17:17:59'),(10,'Manuel','Perera','mp@mail.com','$2b$12$VAHdWNKLKa9c4Ovwe9/YIO0I9hmozeLYXgAtIYlooHrBykrxeCWEe','user',0,0,0,0,0,'','',0,'2025-04-30 11:40:31','2025-05-08 00:16:46'),(11,'Roberto','Alvarez','ra@aventures.com.br','$2b$12$TERC3U4YcjVATMzQ1K1/AODSdhixeJVOiHWpeCP/UKs/w7OeWIeP2','admin',0,0,0,0,0,'','',0,'2025-04-30 11:41:34','2025-05-03 17:12:50');
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

-- Dump completed on 2025-05-12  1:57:40
