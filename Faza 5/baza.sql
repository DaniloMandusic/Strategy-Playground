CREATE DATABASE  IF NOT EXISTS `strategy_playground` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `strategy_playground`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: strategy_playground
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add podaciotrzistu',6,'add_podaciotrzistu'),(22,'Can change podaciotrzistu',6,'change_podaciotrzistu'),(23,'Can delete podaciotrzistu',6,'delete_podaciotrzistu'),(24,'Can view podaciotrzistu',6,'view_podaciotrzistu'),(25,'Can add registration request',7,'add_registrationrequest'),(26,'Can change registration request',7,'change_registrationrequest'),(27,'Can delete registration request',7,'delete_registrationrequest'),(28,'Can view registration request',7,'view_registrationrequest'),(29,'Can add korisnik',8,'add_korisnik'),(30,'Can change korisnik',8,'change_korisnik'),(31,'Can delete korisnik',8,'delete_korisnik'),(32,'Can view korisnik',8,'view_korisnik'),(33,'Can add strategija',9,'add_strategija'),(34,'Can change strategija',9,'change_strategija'),(35,'Can delete strategija',9,'delete_strategija'),(36,'Can view strategija',9,'view_strategija'),(37,'Can add simulacija',10,'add_simulacija'),(38,'Can change simulacija',10,'change_simulacija'),(39,'Can delete simulacija',10,'delete_simulacija'),(40,'Can view simulacija',10,'view_simulacija'),(41,'Can add rang lista',11,'add_ranglista'),(42,'Can change rang lista',11,'change_ranglista'),(43,'Can delete rang lista',11,'delete_ranglista'),(44,'Can view rang lista',11,'view_ranglista');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_korisnik_idKor` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_korisnik_idKor` FOREIGN KEY (`user_id`) REFERENCES `korisnik` (`idKor`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(8,'StrategyPlayground','korisnik'),(6,'StrategyPlayground','podaciotrzistu'),(11,'StrategyPlayground','ranglista'),(7,'StrategyPlayground','registrationrequest'),(10,'StrategyPlayground','simulacija'),(9,'StrategyPlayground','strategija');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-06-05 10:07:25.480048'),(2,'contenttypes','0002_remove_content_type_name','2023-06-05 10:07:25.511322'),(3,'auth','0001_initial','2023-06-05 10:07:25.674615'),(4,'auth','0002_alter_permission_name_max_length','2023-06-05 10:07:25.705771'),(5,'auth','0003_alter_user_email_max_length','2023-06-05 10:07:25.705771'),(6,'auth','0004_alter_user_username_opts','2023-06-05 10:07:25.721395'),(7,'auth','0005_alter_user_last_login_null','2023-06-05 10:07:25.721395'),(8,'auth','0006_require_contenttypes_0002','2023-06-05 10:07:25.737042'),(9,'auth','0007_alter_validators_add_error_messages','2023-06-05 10:07:25.737042'),(10,'auth','0008_alter_user_username_max_length','2023-06-05 10:07:25.737042'),(11,'auth','0009_alter_user_last_name_max_length','2023-06-05 10:07:25.752641'),(12,'auth','0010_alter_group_name_max_length','2023-06-05 10:07:25.768267'),(13,'auth','0011_update_proxy_permissions','2023-06-05 10:07:25.768267'),(14,'auth','0012_alter_user_first_name_max_length','2023-06-05 10:07:25.783920'),(15,'StrategyPlayground','0001_initial','2023-06-05 10:07:26.175965'),(16,'StrategyPlayground','0002_ranglista','2023-06-05 10:07:26.253996'),(17,'admin','0001_initial','2023-06-05 10:07:26.347748'),(18,'admin','0002_logentry_remove_auto_add','2023-06-05 10:07:26.347748'),(19,'admin','0003_logentry_add_action_flag_choices','2023-06-05 10:07:26.363472'),(20,'sessions','0001_initial','2023-06-05 10:07:26.394650'),(21,'StrategyPlayground','0003_alter_simulacija_id_sim','2023-06-05 16:14:46.275146'),(22,'StrategyPlayground','0004_alter_podaciotrzistu_imefajla','2023-06-05 17:01:40.104361'),(23,'StrategyPlayground','0005_alter_strategija_id_strat','2023-06-06 14:29:17.852375'),(24,'StrategyPlayground','0006_alter_podaciotrzistu_idpodtr','2023-06-06 18:42:31.975732'),(25,'StrategyPlayground','0007_alter_strategija_imefajla','2023-06-06 21:00:55.889156'),(26,'StrategyPlayground','0008_alter_simulacija_status','2023-06-06 21:25:11.000662');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('vngazgshdwqptmtuyfsgnuq7tappf5it','.eJxVjDsOwjAQBe_iGln-rjeU9DmDtbYXHECOFCcV4u4QKQW0b2beS0Ta1hq3zkucijgLK06_W6L84LaDcqd2m2We27pMSe6KPGiX41z4eTncv4NKvX5rVkkZdAqA0oCEmMAPKQCwLt6BJbAZ0QRTSHskH4yloHQx2YFzVxbvD8DaNug:1q6dqK:ei_BZsj4SxtkyzIrQbKsCuo2r1dKr4Wfs9XizLVaqNU','2023-06-20 21:03:52.114288');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik`
--

DROP TABLE IF EXISTS `korisnik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik` (
  `password` varchar(128) NOT NULL,
  `idKor` int NOT NULL AUTO_INCREMENT,
  `ime` varchar(20) NOT NULL,
  `prezime` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `odobren` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`idKor`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik`
--

LOCK TABLES `korisnik` WRITE;
/*!40000 ALTER TABLE `korisnik` DISABLE KEYS */;
INSERT INTO `korisnik` VALUES ('pbkdf2_sha256$600000$vAVtZO3xqPfviKnsvHZJ3R$IThNokVkGygz7/NaQoAlB/pFaFpDj0y9OmdeBKCrUoI=',1,'admin','admin','admin@admin.com',0,1,'2023-06-06 21:01:46.496158',1,'2023-06-05 10:08:36.189098',1,'Pending'),('pbkdf2_sha256$600000$37L8y7e3AvO33x05N3Vquf$S+rZJ6lbSidUoQ/0I3cD3lxV2UVaswtOaeRtQBAXDZQ=',2,'Pera','Peric','pera@gmail.com',0,0,'2023-06-05 21:12:54.827110',0,'2023-06-05 10:09:36.980187',1,'Approved'),('pbkdf2_sha256$600000$IUzysKvEozIj8DJ5Vb34FF$QQ5VsTyOUPv5nj4LOojlwG6UXWDCR5hJeN6RBwbSPc8=',3,'Zika','Zikic','zika@gmail.com',0,0,'2023-06-06 21:03:52.111425',0,'2023-06-06 20:59:57.242207',1,'Approved');
/*!40000 ALTER TABLE `korisnik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik_groups`
--

DROP TABLE IF EXISTS `korisnik_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `korisnik_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `korisnik_groups_korisnik_id_group_id_8c5ba7f0_uniq` (`korisnik_id`,`group_id`),
  KEY `korisnik_groups_group_id_639f924a_fk_auth_group_id` (`group_id`),
  CONSTRAINT `korisnik_groups_group_id_639f924a_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `korisnik_groups_korisnik_id_b99df0b8_fk_korisnik_idKor` FOREIGN KEY (`korisnik_id`) REFERENCES `korisnik` (`idKor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik_groups`
--

LOCK TABLES `korisnik_groups` WRITE;
/*!40000 ALTER TABLE `korisnik_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `korisnik_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `korisnik_user_permissions`
--

DROP TABLE IF EXISTS `korisnik_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `korisnik_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `korisnik_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `korisnik_user_permission_korisnik_id_permission_i_f0bb31ce_uniq` (`korisnik_id`,`permission_id`),
  KEY `korisnik_user_permis_permission_id_ed48e217_fk_auth_perm` (`permission_id`),
  CONSTRAINT `korisnik_user_permis_permission_id_ed48e217_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `korisnik_user_permissions_korisnik_id_420accdf_fk_korisnik_idKor` FOREIGN KEY (`korisnik_id`) REFERENCES `korisnik` (`idKor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `korisnik_user_permissions`
--

LOCK TABLES `korisnik_user_permissions` WRITE;
/*!40000 ALTER TABLE `korisnik_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `korisnik_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `podaciotrzistu`
--

DROP TABLE IF EXISTS `podaciotrzistu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `podaciotrzistu` (
  `idPodTr` int NOT NULL AUTO_INCREMENT,
  `imeFajla` varchar(150) NOT NULL,
  `idKor` int NOT NULL,
  PRIMARY KEY (`idPodTr`),
  KEY `podaciotrzistu_idKor_46692a33_fk_korisnik_idKor` (`idKor`),
  CONSTRAINT `podaciotrzistu_idKor_46692a33_fk_korisnik_idKor` FOREIGN KEY (`idKor`) REFERENCES `korisnik` (`idKor`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `podaciotrzistu`
--

LOCK TABLES `podaciotrzistu` WRITE;
/*!40000 ALTER TABLE `podaciotrzistu` DISABLE KEYS */;
INSERT INTO `podaciotrzistu` VALUES (1,'f1/pera1.csv',2),(3,'admin1.csv',1),(4,'admin2.csv',1),(5,'admin3.csv',1),(10,'StrategyPlayground/static/pera_gmail.com/PodaciOCeni/data.csv',2),(11,'StrategyPlayground/static/pera_gmail.com/PodaciOCeni/EURUSD_Ticks_01.05.2023-01.05.2023.csv',2),(12,'StrategyPlayground/static/pera_gmail.com/PodaciOCeni/GBPUSD_Candlestick_1_D_BID_01.04.2023-03.06.2023.csv',2),(14,'StrategyPlayground/static/admin_admin.com/PodaciOCeni/data.csv',1);
/*!40000 ALTER TABLE `podaciotrzistu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rang_lista`
--

DROP TABLE IF EXISTS `rang_lista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rang_lista` (
  `id_rangliste` int NOT NULL AUTO_INCREMENT,
  `naziv` varchar(100) NOT NULL,
  `idPodTr` int NOT NULL,
  PRIMARY KEY (`id_rangliste`),
  KEY `rang_lista_idPodTr_6b42a892_fk` (`idPodTr`),
  CONSTRAINT `rang_lista_idPodTr_6b42a892_fk` FOREIGN KEY (`idPodTr`) REFERENCES `podaciotrzistu` (`idPodTr`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rang_lista`
--

LOCK TABLES `rang_lista` WRITE;
/*!40000 ALTER TABLE `rang_lista` DISABLE KEYS */;
INSERT INTO `rang_lista` VALUES (1,'Rang Lista 1',14),(2,'Rang Lista 2',4),(3,'asd',4);
/*!40000 ALTER TABLE `rang_lista` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `simulacija`
--

DROP TABLE IF EXISTS `simulacija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `simulacija` (
  `id_sim` int NOT NULL AUTO_INCREMENT,
  `ime` varchar(50) NOT NULL,
  `status` varchar(1000) NOT NULL,
  `idPodTr` int NOT NULL,
  `idStrat` int NOT NULL,
  PRIMARY KEY (`id_sim`),
  KEY `simulacija_idStrat_f3c35d52_fk` (`idStrat`),
  KEY `simulacija_idPodTr_d2990b47_fk` (`idPodTr`),
  CONSTRAINT `simulacija_idPodTr_d2990b47_fk` FOREIGN KEY (`idPodTr`) REFERENCES `podaciotrzistu` (`idPodTr`),
  CONSTRAINT `simulacija_idStrat_f3c35d52_fk` FOREIGN KEY (`idStrat`) REFERENCES `strategija` (`id_strat`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `simulacija`
--

LOCK TABLES `simulacija` WRITE;
/*!40000 ALTER TABLE `simulacija` DISABLE KEYS */;
INSERT INTO `simulacija` VALUES (2,'sim3','{\"status\": \"success\", \"score\": 1070.0}',14,2),(3,'sim3','{\"status\": \"success\", \"score\": 1040.0}',14,3),(4,'sim4','{\"status\": \"pending\"}',3,3),(57,'asd','{\"status\": \"failure\", \"msg\": \"Traceback (most recent call last):\\n  File \\\"C:\\\\Dev\\\\project_TimBezImena\\\\Faza 5\\\\Backtester\\\\Tester\\\\views.py\\\", line 30, in run\\n    result = self.backtest.run()\\n             ^^^^^^^^^^^^^^^^^^^\\n  File \\\"C:\\\\Dev\\\\project_TimBezImena\\\\Faza 5\\\\Backtester\\\\Tester\\\\backtest.py\\\", line 96, in run\\n    self.strategy.process_tick(tick, self.buy, self.sell)\\n    ^^^^^^^^^^^^^^^^^^^^^^^^^^\\nAttributeError: \'Strategy\' object has no attribute \'process_tick\'\\n\"}',14,11),(61,'asdf','{\"status\": \"failure\", \"msg\": \"Traceback (most recent call last):\\n  File \\\"C:\\\\Dev\\\\project_TimBezImena\\\\Faza 5\\\\Backtester\\\\Tester\\\\views.py\\\", line 30, in run\\n    result = self.backtest.run()\\n             ^^^^^^^^^^^^^^^^^^^\\n  File \\\"C:\\\\Dev\\\\project_TimBezImena\\\\Faza 5\\\\Backtester\\\\Tester\\\\backtest.py\\\", line 97, in run\\n    self._update_open_positions(tick)\\n  File \\\"C:\\\\Dev\\\\project_TimBezImena\\\\Faza 5\\\\Backtester\\\\Tester\\\\backtest.py\\\", line 79, in _update_open_positions\\n    if position.direction == \'buy\' and tick[\'price\'] >= position.take_profit:\\n                                       ~~~~^^^^^^^^^\\nKeyError: \'price\'\\n\"}',14,11),(62,'asdff','{\"score\": 1060.0, \"open_positions\": [], \"closed_positions\": [{\"type\": \"buy\", \"entry\": 90.08526, \"tp\": 110.08526, \"sl\": 85.08526, \"risk\": 0.02, \"closed\": true, \"closing_time\": \"15.05.2023 00:03:00.000\"}, {\"type\": \"sell\", \"entry\": 100.08426, \"tp\": 80.08426, \"sl\": 105.08426, \"risk\": 0.02, \"closed\": true, \"closing_time\": \"15.05.2023 00:04:00.000\"}], \"status\": \"success\"}',14,11);
/*!40000 ALTER TABLE `simulacija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `strategija`
--

DROP TABLE IF EXISTS `strategija`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `strategija` (
  `id_strat` int NOT NULL AUTO_INCREMENT,
  `imeFajla` varchar(150) NOT NULL,
  `idKor` int NOT NULL,
  PRIMARY KEY (`id_strat`),
  KEY `strategija_idKor_d7bbf955_fk_korisnik_idKor` (`idKor`),
  CONSTRAINT `strategija_idKor_d7bbf955_fk_korisnik_idKor` FOREIGN KEY (`idKor`) REFERENCES `korisnik` (`idKor`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `strategija`
--

LOCK TABLES `strategija` WRITE;
/*!40000 ALTER TABLE `strategija` DISABLE KEYS */;
INSERT INTO `strategija` VALUES (2,'C:\\Dev\\project_TimBezImena\\Faza 5\\Backtester\\Tester\\some_folder\\example_strategy.py',2),(3,'admin_strat.py',1),(9,'C:\\Dev\\project_TimBezImena\\Faza 5\\Projekat\\StrategyPlayground\\static\\pera_gmail.com\\strategije\\test',2),(11,'C:\\Dev\\project_TimBezImena\\Faza 5\\Projekat\\StrategyPlayground\\static\\zika_gmail.com\\strategije\\strat.py',3);
/*!40000 ALTER TABLE `strategija` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `strategyplayground_registrationrequest`
--

DROP TABLE IF EXISTS `strategyplayground_registrationrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `strategyplayground_registrationrequest` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ime` varchar(20) NOT NULL,
  `prezime` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `strategyplayground_registrationrequest`
--

LOCK TABLES `strategyplayground_registrationrequest` WRITE;
/*!40000 ALTER TABLE `strategyplayground_registrationrequest` DISABLE KEYS */;
/*!40000 ALTER TABLE `strategyplayground_registrationrequest` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-06 23:43:49
