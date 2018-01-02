-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.1.23-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             9.4.0.5125
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for coinmarketcap
CREATE DATABASE IF NOT EXISTS `coinmarketcap` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `coinmarketcap`;

-- Dumping structure for table coinmarketcap.coin_tbl
CREATE TABLE IF NOT EXISTS `coin_tbl` (
  `coinID` int(11) NOT NULL,
  `symbol` varchar(7) NOT NULL,
  `name` varchar(255) NOT NULL,
  `link` varchar(1000) NOT NULL,
  `webpage` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='un id\r\nle symbol\r\nle name';

-- Dumping data for table coinmarketcap.coin_tbl: ~0 rows (approximately)
/*!40000 ALTER TABLE `coin_tbl` DISABLE KEYS */;
/*!40000 ALTER TABLE `coin_tbl` ENABLE KEYS */;

-- Dumping structure for table coinmarketcap.price_tbl
CREATE TABLE IF NOT EXISTS `price_tbl` (
  `coinID` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table coinmarketcap.price_tbl: ~0 rows (approximately)
/*!40000 ALTER TABLE `price_tbl` DISABLE KEYS */;
/*!40000 ALTER TABLE `price_tbl` ENABLE KEYS */;

-- Dumping structure for table coinmarketcap.supply_tbl
CREATE TABLE IF NOT EXISTS `supply_tbl` (
  `coinID` int(11) DEFAULT NULL,
  `supply` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Dumping data for table coinmarketcap.supply_tbl: ~0 rows (approximately)
/*!40000 ALTER TABLE `supply_tbl` DISABLE KEYS */;
/*!40000 ALTER TABLE `supply_tbl` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
