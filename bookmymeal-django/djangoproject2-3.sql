-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 07, 2019 at 04:55 PM
-- Server version: 5.7.27-0ubuntu0.16.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `djangoproject2-3`
--

-- --------------------------------------------------------

--
-- Table structure for table `addcat`
--

CREATE TABLE `addcat` (
  `catid` int(11) NOT NULL,
  `catnm` varchar(50) NOT NULL,
  `caticonnm` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addcat`
--

INSERT INTO `addcat` (`catid`, `catnm`, `caticonnm`) VALUES
(1, 'Indian', 'indianfood.png'),
(2, 'Italian', 'italian.jpeg'),
(3, 'Maxican', 'maxican.png'),
(4, 'Chinese', 'chinese.png');

-- --------------------------------------------------------

--
-- Table structure for table `addsubcat`
--

CREATE TABLE `addsubcat` (
  `subcatid` int(11) NOT NULL,
  `subcatnm` varchar(50) NOT NULL,
  `catnm` varchar(50) NOT NULL,
  `subcaticonnm` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addsubcat`
--

INSERT INTO `addsubcat` (`subcatid`, `subcatnm`, `catnm`, `subcaticonnm`) VALUES
(1, 'Rajasthani', 'Indian', 'rj.jpeg'),
(2, 'Southindian', 'Indian', 'south.png'),
(3, 'Sizzlers', 'Chinese', 'ch1.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `foodproduct`
--

CREATE TABLE `foodproduct` (
  `pid` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `subcatnm` varchar(50) NOT NULL,
  `description` varchar(1000) NOT NULL,
  `price` int(11) NOT NULL,
  `foodicon` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `foodproduct`
--

INSERT INTO `foodproduct` (`pid`, `title`, `subcatnm`, `description`, `price`, `foodicon`) VALUES
(1, 'Dish1', 'Rajasthani', 'good quality product', 50, 'ch8.jpg'),
(2, 'Dish2', 'Rajasthani', 'product at affordable price', 150, '406.jpg'),
(3, 'Dish3', 'Sizzlers', 'seasonal veggies added', 210, '99.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `txnid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `uid` varchar(100) NOT NULL,
  `dt` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`txnid`, `pid`, `price`, `uid`, `dt`) VALUES
(1, 1, 50, 'adawadkarvilekh@gmail.com', 'Thu Aug  1 09:42:47 2019'),
(2, 2, 150, 'adawadkarvilekh@gmail.com', 'Thu Aug  1 09:45:47 2019'),
(3, 1, 50, 'phpbatch34@gmail.com', 'Wed Aug  7 11:21:25 2019');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `regid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(10) NOT NULL,
  `mobile` varchar(15) NOT NULL,
  `address` varchar(1000) NOT NULL,
  `city` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `role` varchar(10) NOT NULL,
  `status` int(11) NOT NULL,
  `dt` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`regid`, `name`, `email`, `password`, `mobile`, `address`, `city`, `gender`, `role`, `status`, `dt`) VALUES
(1, 'vilekh adawadkar', 'adawadkarvilekh@gmail.com', '123', '9752155505', 'rambag indore', 'Indore', 'male', 'user', 1, 'Tue Jul 23 09:33:19 2019'),
(2, 'Admin', 'admin@gmail.com', '12345', '1111111111', 'check address', 'Bhopal', 'female', 'admin', 1, 'Tue Jul 23 09:35:07 2019'),
(4, 'bhavishya', 'bhavishyarathore06@gmail.com', '123', '9039167363', 'betul', 'Indore', 'male', 'user', 1, 'Wed Aug  7 11:10:05 2019'),
(5, 'phpbatch34', 'phpbatch34@gmail.com', '12345', '1111111111', 'indore mp', 'Indore', 'female', 'user', 1, 'Wed Aug  7 11:15:40 2019');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addcat`
--
ALTER TABLE `addcat`
  ADD PRIMARY KEY (`catid`);

--
-- Indexes for table `addsubcat`
--
ALTER TABLE `addsubcat`
  ADD PRIMARY KEY (`subcatid`),
  ADD UNIQUE KEY `subcatnm` (`subcatnm`);

--
-- Indexes for table `foodproduct`
--
ALTER TABLE `foodproduct`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`txnid`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`regid`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addcat`
--
ALTER TABLE `addcat`
  MODIFY `catid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `addsubcat`
--
ALTER TABLE `addsubcat`
  MODIFY `subcatid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `foodproduct`
--
ALTER TABLE `foodproduct`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `txnid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `regid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
