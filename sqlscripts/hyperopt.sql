-- MySQL dump 10.13  Distrib 8.0.26, for Linux (x86_64)
--
-- Host: localhost    Database: hyperopt
-- ------------------------------------------------------
-- Server version	8.0.26-0ubuntu0.21.04.3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `runAncestry`
--

DROP TABLE IF EXISTS `runAncestry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `runAncestry` (
  `Session` int DEFAULT NULL,
  `runID` int NOT NULL AUTO_INCREMENT,
  `Generation` int DEFAULT NULL,
  `PopulationMember` int DEFAULT NULL,
  `aParam` int DEFAULT NULL,
  `bParam` int DEFAULT NULL,
  `cParam` int DEFAULT NULL,
  `dParam` int DEFAULT NULL,
  `eParam` int DEFAULT NULL,
  `fParam` int DEFAULT NULL,
  `rParam` int DEFAULT NULL,
  `xParam` int DEFAULT NULL,
  `Timeout` int DEFAULT NULL,
  `zParam` VARCHAR(50),
  `iParam` VARCHAR(50),
  `wParam` VARCHAR(50),
  `EndScore` FLOAT DEFAULT NULL,
  `StartScore` FLOAT DEFAULT NULL,
  `StartTime` FLOAT DEFAULT NULL,
  `EndTime` FLOAT DEFAULT NULL,
  `P1` FLOAT DEFAULT NULL,
  `P2` FLOAT DEFAULT NULL,
  `P3` FLOAT DEFAULT NULL,
  PRIMARY KEY (`runID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `runAncestry`
--

LOCK TABLES `runAncestry` WRITE;
/*!40000 ALTER TABLE `runAncestry` DISABLE KEYS */;
INSERT INTO `runAncestry` VALUES (1,10,20,30,40,50,60,70,'test1.wcard',100);
/*!40000 ALTER TABLE `runAncestry` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-09-18 16:54:48
