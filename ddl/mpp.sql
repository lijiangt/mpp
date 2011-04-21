-- MySQL dump 10.13  Distrib 5.1.49, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: mpp
-- ------------------------------------------------------
-- Server version	5.1.49-1ubuntu8.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `mpp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `mpp` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `mpp`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_fbfc09f1` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add Category',9,'add_category'),(26,'Can change Category',9,'change_category'),(27,'Can delete Category',9,'delete_category'),(28,'admin for cms module',9,'can_admin'),(29,'Can add Article',10,'add_article'),(30,'Can change Article',10,'change_article'),(31,'Can delete Article',10,'delete_article'),(32,'Can add Feedback',11,'add_feedback'),(33,'Can change Feedback',11,'change_feedback'),(34,'Can delete Feedback',11,'delete_feedback'),(35,'Can add Feature Suggest',12,'add_suggestfeature'),(36,'Can change Feature Suggest',12,'change_suggestfeature'),(37,'Can delete Feature Suggest',12,'delete_suggestfeature'),(38,'Can add building',13,'add_building'),(39,'Can change building',13,'change_building'),(40,'Can delete building',13,'delete_building'),(41,'Can add department',14,'add_department'),(42,'Can change department',14,'change_department'),(43,'Can delete department',14,'delete_department'),(44,'Can add sub department',15,'add_subdepartment'),(45,'Can change sub department',15,'change_subdepartment'),(46,'Can delete sub department',15,'delete_subdepartment');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','','','lijt@bupt.edu.cn','sha1$6cacc$916df9ceb03f02c9e68fe04d6b567dfd5bd70e64',1,1,1,'2011-04-17 16:33:17','2011-03-17 16:11:55');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_article`
--

DROP TABLE IF EXISTS `cms_article`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `pic` varchar(100) DEFAULT NULL,
  `type` smallint(6) NOT NULL,
  `category_id` int(11) NOT NULL,
  `viewTimes` bigint(20) NOT NULL,
  `posted` datetime NOT NULL,
  `lastModified` datetime NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `setTop` smallint(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`,`category_id`),
  KEY `cms_article_42dc49bc` (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_article`
--

LOCK TABLES `cms_article` WRITE;
/*!40000 ALTER TABLE `cms_article` DISABLE KEYS */;
INSERT INTO `cms_article` VALUES (1,'安保信息','校园110：','',10,7,0,'2011-03-31 14:15:40','2011-03-31 14:15:40',NULL,0),(2,'班车信息','一、校本部 至 宏福校区每周一至周五，<br />　　早7：00校本部同时发2部车（大金龙）<br />　　上午8：40校本部发1部车（大金龙）<br />　　中午12：30校本部发1部车（大金龙）<br /><br /><br />二、宏福校区 至 校本部<br />每周一至周五<br />　　上午10：10 宏福校区发1部车（大金龙）<br />　　中午12：30宏福校区发1部车（大金龙）<br />　　下午4：40宏福校区发1部车（大金龙）<br />　　下午5：40宏福校区发1部车（大金龙）<br /><br /><br />三、每周二、四晚班车<br />　　下午5：00校本部发1部车（小面包），晚8：40返回。<br /><br /><br />四、发车地点<br />　　校本部发车地点：教三楼西侧<br /><p>　　宏福校区发车地点：综合办公楼西侧&nbsp;</p><p><img src=\"/s/upload/2011/104/15/map.png\" alt=\"\" /><br /></p>','',10,6,0,'2011-03-31 14:16:03','2011-04-14 15:54:39',NULL,0),(3,'北邮办公布告栏','','',30,2,0,'2011-03-31 14:17:02','2011-03-31 14:17:02','http://buptoa.bupt.edu.cn/',0),(4,'北邮人','','',30,2,0,'2011-03-31 14:17:41','2011-03-31 14:17:41','http://www.byr.edu.cn/',0),(5,'北邮主页','','',30,2,0,'2011-03-31 14:18:02','2011-03-31 14:18:02','http://www.bupt.edu.cn/',2),(6,'学校简介','北京邮电大学是教育部直属、工业和信息化部共建、首批进行“211工程”建设的全国重点大学，是一所以信息科技为特色、工学门类为主体、工管文理相结合的多科性大学，是我国信息科技人才的重要培养基地。<br /><br /><br />自1955年建校以来，经过半个多世纪的建设与发展，学校全日制教育已经形成了信息背景浓郁、专业特色鲜明、学科优势突出的办学格局。学校现设有信息与通信工程学院、电子工程学院、计算机学院、自动化学院、软件学院、经济管理学院、人文学院、理学院、国际学院、网络教育学院（继续教育学院）、民族教育学院和马克思主义教学与研究中心、体育部等13个教学单位，以及网络技术、信息光子学与光通信、感知技术与产业3个研究院，并设有研究生院。目前，学科专业已经涵盖理学、工学、文学、法学、经济学、管理学、军事学、教育学、哲学等9个学科门类，涉及22个一级学科。学校现有全日制本、硕、博学生及留学生共约21000名，正式注册的非全日制学生约28000名。<br /><br /><br />近几年来，北京邮电大学坚持以科学发展观为指导，按照经济社会的发展需求，遵循高等教育的办学规律，制定了“两翼齐飞，四轮驱动”的总体发展战略，启动了学校的全面改革。在全校党员、全体师生的共同努力下，学校的改革与发展进入了一个新的阶段。<br /><br /><br />——牢固确立人才培养是高等学校的根本任务的思想，大力推进实施“质量工程”，积极推进本科教育教学改革和研究生培养机制创新，实现了质量与规模的协调发展。2008年3月，教育部正式公布我校以“优秀”成绩通过“本科教学工作水平评估”，标志着我校人才培养质量踏上了新的台阶。近三年，我校在全国百篇优秀博士学位论文、国家精品课程、北京市精品课程、国家级双语教学示范课程、普通高等教育精品教材、国家级教学团队、北京市优秀教学团队、国家级教育成果奖、北京市教育成果奖等各级各类评选工作中均取得了良好的成绩。长期以来，我校学生大学英语四级一次通过率保持在80%以上，六级年级累计通过率保持在60%以上。研究生就业率始终保持为100%，本科生就业率保持在98%以上。在以英语、电子、数学和物理竞赛为代表的国内外大学生重大赛事中成绩优异，位居全国重点高校前列。<br /><br /><br />——始终坚持办学以教师为根本的指导思想，积极推进“人才工程”，人才队伍不断壮大，师资结构不断优化。目前，我校拥有着一支以国家自然科学基金委创新研究群体、“长江学者和创新团队发展计划”创新团队、“新世纪百千万人才工程”国家级人选、国家级突出贡献专家、“国家杰出青年科学基金”获得者、教育部“跨世纪优秀人才计划”获得者、“新世纪优秀人才支持计划”获得者、北京市优秀教学团队、北京市科技新星、省部级“青年学科带头人”、省部级“优秀青年骨干教师”、政府特殊津贴专家、国家级教学名师等为骨干的实力雄厚的师资队伍。在学校专任教师中，共有院士11人，具有正、副高职称的教师600余人，具有博士、硕士学位的教师占专任教师总数的85.8%。<br /><br /><br />——以“211工程”建设和两个“111”学科创新引智基地建设为重点，不断加强学科建设，学科布局进一步优化。目前，学校具有博士、硕士整体授予权的一级学科8个，一级学科博士后科研流动站5个，博士学位授权点15个，硕士学位授权点45个。现有35个本科专业，42个硕士专业。学科涵盖了理、工、文、法、哲、经济、管理、军事、教育等9个学科门类，初步形成了信息学科优势突出、工管文理相互支撑的多科性学科架构。在重点学科建设方面，2007年，我校获得电子科学与技术、信息与通信工程两个一级学科国家重点学科认定。2007年以来启动了特色专业建设工作，获批国家级特色专业4个，北京市特色专业8个。<br /><br /><br />——加强基地建设，科研工作良性发展。我校建有以国家重点实验室、国家工程实验室、教育部重点实验室 、教育部国防重点实验室、教育部工程研究中心、教育部学科创新引智基地为代表的若干高水平的科研基地。以基地建设和团队建设为基础，我校科研工作在质和量两个方面呈现出快速增长态势。科研经费增长迅速，科学研究成果频出，近三年共获得国家科技发明奖、国家科技进步奖、省部级及社会力量奖三十余项。同时，我校建有国家级大学科技园，为推进科技成果转化奠定了良好基础。<br /><br /><br />——加强国际合作与交流，国际化办学水平进一步提高。2004年，经教育部批准，我校开始实施与伦敦大学玛丽女王学院的学士学位联合培养项目，成立了国际学院。四年来，国际学院以其严格的管理和高水平的人才培养质量在全社会引起广泛好评。在学生联合培养工作方面，我校与国外60余所知名大学、国际性企业及科研机构签署了学生培养交流合作协议或备忘录近100余项，建立和启动交流项目40余个，涉及30多个国家和地区、近40个高水平大学。依托“电磁场与微波技术”和“通信与信息系统”两个国家重点学科，成功申报和建设了“通信与网络核心技术创新引智基地”和“高等智能与网络服务创新引智基地”两个国家“111”创新引智基地，引进了以诺贝尔物理学奖获得者若尔斯.阿尔费罗夫为代表的世界一流学术大师和科研学者，形成了实力强大的国际化研究阵容。积极主办高层次、高规格国际会议，搭建学校与国际高水平大学的学术交流平台，增进了学校与国际高水平大学的学术交流与对话，进一步提升了学校的国际影响力。<br /><br /><br />北京邮电大学在“团结 勤奋 严谨 创新”的校风、“厚德 博学 敬业 乐群”的校训和“崇尚奉献、追求卓越”的北邮精神的引领下，正朝着在本世纪中叶（建校100周年）建成信息科技特色突出，工管文理协调发展的世界高水平特色型大学这一宏伟目标而阔步前进。','',10,12,0,'2011-04-07 16:21:38','2011-04-13 14:31:58',NULL,0),(15,'警情提示（2011年第3期）','<br /><br /><br />新学期伊始，是各类诈骗、偷窃案件的高发时期。为了维护学校良好的治安秩序，防止师生员工个人财产遭受侵害，现将犯罪分子常用诈骗、偷窃手段及需要防范的内容提示给大家，请广大师生员工在日常学习、生活中加以防范。&nbsp;<br />一、犯罪嫌疑人冒充特定身分（如学生、老乡等），谎称外出遇难或家庭困难，骗取同情，直接骗取钱财。 发生此类事情一定要核实清楚后给与帮助，不要随意相信，也不要随意给与钱财。<br />二、犯罪嫌疑人以信用卡失窃或丢失为名，谎称急需用钱，借用事主信用卡异地存取，骗取信用卡及密码、手机等，随后将卡中现金骗取。对于陌生人提出此类要求不要理睬，并及时报案。<br />三、犯罪嫌疑人通过伪造网站、网页，骗取事主信用卡号及密码，再通过网上银行将事主卡中现金转走。不要随意将自己的信用卡号及密码泄漏给他人，发生此类案件应及时报案，&nbsp;<br />四、犯罪嫌疑人利用群发中奖信息，以邮寄奖品需要邮费或缴纳所得税等为借口，提供账号，骗得事主汇款或转账。发生此类事情一定要核实清楚，要货到付款。<br />五、犯罪嫌疑人通过各种渠道获取学生私人信息，给学生家长打电话，谎称其孩子遭意外，需手术缴费，骗得家长汇款或转帐。各位同学一定要与家长沟通，提示接到类似情况时要核实清楚，不要随意给对方汇款。<br />六、犯罪嫌疑人在互联网上伪称出售低价手机、笔记本电脑等，提供账号让事主汇款或转账。网上购物不要贪图便宜，一定要找有信用的卖家，货到付款。&nbsp;<br />七、犯罪嫌疑人利用群发短信，称事主信用卡在外地被透支消费，需要将卡内现金转入安全帐号，进行诈骗。有此类情况发生不要理睬。<br />八、犯罪分子利用网络、手机发布信息发放低息贷款。发现此类信息不要相信，不要随意借贷，确有急需贷款应到国家金融机构办理。<br />九、犯罪嫌疑人在 ATM 机上假冒银行名义，张贴虚假升级告示，然后诱导事主进行一系列的操作，最终将事主卡内资金转走；或利用事主在 ATM 机取钱时，转移事主注意力，将事先准备好的废卡插入卡口内，待事主误以为卡已退出离开后，犯罪嫌疑人继续对事主信用卡进行操作，窃取钱财。目前犯罪嫌疑人利用 ATM 机作案的方法不断翻新，令人防不胜防，因此凡出现违反常规程序的操作，大家要提高警惕。如已进行操作，应立即与银行联系，及时更改密码信息，发现钱财已经被冒领应及时报案。<br />我校学生时常发生在课间打水、打电话、去卫生间期间或在食堂吃饭期间发生贵重物品丢失现象，为此，保卫处提醒同学们要加强自我保护意识，在外出期间要将贵重物品随身携带，如外出时间较短，一定要委托熟悉的同学代为看管，切不可将手机、钱包等贵重财物随意放置于桌上离开，给不法分子以可乘之机。去食堂吃饭时书包应随身携带，不要放置在餐椅上占座，吃饭时应将装有贵重物品的书包放置在视线之内。','',10,14,0,'2011-04-13 14:44:41','2011-04-13 14:44:41',NULL,0),(7,'历史沿革','北京邮电大学创建于1955年，原名北京邮电学院，是以天津大学电讯系、电话电报通讯和无线电通信广播两个专业及重庆大学电机系电话电报通讯专业为基础组建的，是新中国第一所邮电高等学府，隶属原邮电部。<br />&nbsp;&nbsp;1959年和1960年北京电信学院及其附属中技部、邮电科技大学先后并入北京邮电学院。1960年北京邮电学院被确定为全国64所重点院校之一。<br />&nbsp;&nbsp;1993年经原国家教委批准，“北京邮电学院”更名为“北京邮电大学”，时任中共中央总书记、国家主席江泽民亲笔题写了校名。<br />&nbsp;&nbsp;1998年北京邮电大学成为全国首批重点建设的61所“211工程”项目院校。<br />&nbsp;&nbsp;1999年成为全国开展远程教育试点的四所院校之一。<br />&nbsp;&nbsp;2000年全国院校调整后，直属国家教育部管理。<br />&nbsp;&nbsp;2004年成为全国56所设立研究生院的高校之一。<br />&nbsp;&nbsp;2005年，教育部和原信息产业部联合签署协议共建北京邮电大学。','',10,11,0,'2011-04-07 16:28:54','2011-04-13 14:33:35',NULL,0),(14,'警情提示（2011年第4期）','警 情 提 示<br />（2011年第4期）<br /><br /><br />2011年1月1日-2月28日，海淀区各类诈骗案件呈现高发态势，且大幅度高于去年同期水平。仅高校学生被诈骗案件发案就有55件，其中：银行卡升级诈骗6件、电话飞信和网络QQ诈骗16件、网络购物诈骗21件、网上购火车票、机票诈骗9件、银行卡遗卡盗取2件、中奖被骗1件。以下是典型案例：<br />1、2011年1月1日17时43分，事主在某高校学生公寓被骗19000元。<br />2、2011年1月11日14时40分，事主在某高校学生公寓收到手机短信后到网上升级银行网银系统，几次未升级成功，后发现卡内少了2800元钱。<br />3、2011年1月15日10时14分，事主在某高校学生公寓上网购买火车票，被对方从卡内骗走2000余元。<br />4、2011年1月22日23时47分，事主在某高校学生公寓上网，一好友通过QQ向事主借钱，事主通过网银转账1200元后，发现被骗。<br />5、2011年1月24日9时34分，事主在某高校学生公寓被网上钓鱼网站骗走5000元钱。<br />6、2011年1月24日15时35分，事主在某高校学生公寓上网时遇到一冒充其同学人员，被骗向其手机内充值100元。<br />7、2011年2月21日15时20分，事主因收到手机中奖信息，在某高校邮局给对方汇款7600元后发现被骗。<br />8、2011年2月21日23时38分，事主在某高校学生公寓上网时被人用其朋友的QQ 号诈骗900元话费。<br />9、2011年2月22日16时05分，事主在某高校学生公寓上网时被一名冒充其朋友的人诈骗，为其购买700元游戏点卡。<br />10、2011年2月22日18时55分，事主在某高校内北京银行ATM机处取款时，将银行卡遗失在ATM机内，被盗取2000元。<br />11、2011年2月23日19时54分，事主在某高校学生公寓内上网时被骗1300元。<br />12、2011年2月25日14时12分，事主在某高校学生公寓网购时被骗2400元。<br />13、2011年2月26日18时47分，事主在某高校学生公寓网购时被骗3300元。<br />鉴于上述发案情况，保卫处提醒广大师生提高警惕，特别是收到手机短信、网络购物、通过网络购买火车票和飞机票，或者在被通知银行卡升级等方面严加防范，注意安全提高警惕，防止上当受骗。','',10,14,0,'2011-04-13 14:39:53','2011-04-13 14:39:53',NULL,0),(8,'领导机构','<p>党委书记：王亚杰</p><p>校长：方滨兴</p><p>党委副书记：赵纪宁 牟文杰</p><p>副校长：张英海 任晓敏 薛忠文 杨放春 温向明</p><p>纪委书记：牟文杰（兼）</p><p>校长助理：汪成楚 吕廷杰 耿 建 刘晓平 宿继军</p><p>党委常委：王亚杰 方滨兴 赵纪宁 牟文杰 张英海 任晓敏 薛忠文 杨放春 温向明 李 杰 曲昭伟</p>','',10,10,0,'2011-04-07 16:29:55','2011-04-07 16:45:27',NULL,0),(9,'叶培大    院士','<p>叶培大    院士&nbsp;</p><p>&nbsp;中国科学院资深院士、北京邮电大学名誉校长、微波通信及光电通信专家。1915年出生于上海市；1938年毕业于天津北洋大学；1945－1946年在美国 哥伦比亚大学研究院就读，其间先后到美国国家广播公司和加拿大北方电气公司实习；1955年从天津大学调入北京邮电学院，历任无线系教授及系主任、院长助 理、副院长、院长、名誉院长、名誉校长。现为北京邮电大学信息光子学与光通信研究院教授。</p><p><br /></p>','pic/2011/097/yepeida.jpg',20,9,0,'2011-04-07 16:48:27','2011-04-07 16:48:27',NULL,0),(10,'陈俊亮    院士','<span style=\"font-family: 宋体, Arial, Verdana, sans-serif; border-collapse: collapse; line-height: 20px; \">中国科学院院士、中国工程院院士、通信与电子系统专家。1931年生人，1955年7月毕业于上海交通大学电讯系，1961年5月获莫斯科电讯工程学院副博 士学位。1978—1981年到美国加州大学UCB做访问学者，同期受聘于 UCBEECS系客座副教授。现为北京邮电大学网络技术研究院院长、教授。</span>','pic/2011/097/2f42ece078b0e5a27d3e0b1c6425140d-chenjunliang.jpg',20,9,0,'2011-04-07 16:52:41','2011-04-07 16:52:41',NULL,0),(11,'常怀爱国之心，常抒爱国之情──方滨兴校长在2011届研究生毕业典礼上的讲话','同学们，大家早上好！<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;今天，我们如期所至地迎来了一年一度的庆贺研究生毕业盛典。当然，对你们来说这是人生中一个很重要的场景：这是一个独特的分别仪式，师生及同学间相互道别，校园里充满着惆怅与不舍；这是一个庄严的宣告仪式，被知识武装起来的你们即将踏入社会，每一个人都在憧憬着美好的未来！<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;刚才，在校同学与老师分别向你们表达了祝福之情，你们也向学校表达了感激之意。现在，请允许我代表学校，向顺利完成学业的2011届近四百名博士生及两千一百名硕士生表示热烈的祝贺！向为你们的成长成才倾注心血和汗水的各位研究生导师、教职员工表示诚挚的感谢！向全力支持同学们完成学业的各位家长和亲友们表示真诚的谢意！（掌声）<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;在你们离校前的最后一次校长演讲中，我感到有非常多的话要说。我想再一次赞美你们在历次大型活动中的出色表现，尤其是在长达数月的北京奥运会和残运会的志愿者经历中，你们为国家赢得了尊严，为北京赢得了微笑，为北邮赢得了声誉，为自己赢得了信赖。我也想借此盘点一下你们留给母校的记忆：例如信通院夏璐等14名同学在研期间申请了16项发明专利；网研院郭少勇、杨新星等19名同学先后21次在全国研究生数学建模竞赛上为北邮赢得了名次。我还想嘱咐你们在今后的道路上，要继续树立远大的理想和高远的境界，修身，齐家，治国，平天下，把自己的成长成才，融入到国家的进步和民族的振兴之中，实现人生更大的价值。（掌声）<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;但是，此时此刻我最想跟你们讲的主题是“爱国”，一是爱国之心，就是要用你们的聪明才智让国家更加强大；二是爱国之情，就是要像爱护眼球一样，维护社会的稳定。<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;首先说一下爱国之心。这两、三个月，世界上发生了一连串的大事。且不说突尼斯、埃及的政体变革，这毕竟是人家的内政；也不说日本的海啸灾害引发的核灾难，毕竟这几年我国也自然灾害频发。我要说的是利比亚，一个小小的国家发生着吸引世界眼球的大事。利比亚反对派发起了一个结果夹生了的反政府运动，面对晕头之后又强势起来的利比亚政府力量，世界列强终于露出了狰狞的嘴脸，他们派出了强大的武装力量，对最高统帅仅仅是上校的弱小军队实施了无情的打击（议论声）。当然，设立禁飞区是联合国授权了的，就是不准有未经联合国授权的飞机在空中飞行。但是，承担禁飞区任务的美法英联军并不这样理解禁飞区的概念，而是借用联合国的授权大肆轰炸利比亚的政府武装力量和军事设施。既然狂轰滥炸不是联合国的授权，我就不再称他们为联合国部队，而是根据出动飞机的情况姑且称之为美法英八国[i]联军，这不由地让我想起一百多年前中国就曾被英法八国联军践踏过；十年内阿富汗、伊拉克也被美英多国联军给祸害的远不如之前宁静。他们具有砸烂一个国家的强大力量，却没有表现出建设好这些国家的责任心。（议论声）<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;我们大家都能看到，利比亚已经陷入到内战状态，美法英八国联军以保护平民不受伤害的名义协助着一方去攻打另一方，反而让战火不断延续下去，恐怕得一直打到让一个合法政府彻底倒台为止，也可能会导致利比亚分裂成两个国家，或长期内战，总之都会遭致更多的生灵涂炭。这将是以保护平民之名开头，以更多平民死于战争之实结尾的又一典范。前南斯拉夫不也是在美英多国联军的连续78天的轰炸中解体了吗？<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;网上有人评价说，现在的世界，列强们先是鼓动别的国家内部自相残杀，然后再帮助这一方去杀另一方，最后可能再把不听话的这一方给除掉。不管怎么说，我们看到的是这样的结果：列强们的逻辑就是世界的逻辑，列强们的道理就是世界的道理。从媒体可以看到俄罗斯总理普京是这样评价这次战争的：“所有这一切都处在保护爱好和平的平民的伪装下。逻辑在哪里？良心在哪里？两样都没有！”“利比亚的情况表明，俄罗斯做出加强自己军力的决定是正确的。”我十分赞同这一观点。一个国家要是不想沦落成利比亚、伊拉克，就必须有强大的自卫实力。国家不强大，就会受欺辱。我们不称霸，但也决不能落到别人想怎么打你就怎么打你的地步！（长时间掌声、欢呼声）强大是需要实力的，这种实力集中体现在科技水平上。因此，报效祖国应该是你们各位的首选。希望你们既要拥有爱国的实力，又能用自己的实力托举起祖国的尊严与强盛！（掌声）<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;其次说一下爱国之情。北非与中东的政局动乱，勾引出反华势力的极大期待。希拉里高调要向中国输出民主；美国驻华大使亲自到网络煽动集会的现场去“打酱油”（掌声笑声），恐怕是指望看见突尼斯场景的再现。境外民运分子更是不断利用互联网来煽动网民采取有计划、有步骤的行动以谋求中国政局的混乱，从而火中取栗。现在的问题是，到底是谁希望中国政局动荡，到底是谁希望中国陷入混乱的泥潭之中？<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;中国现在已经成为世界上第二大经济体了，这难道不算是成功吗？中国经济长期以来以世界上最快的速度增长，西方国家又是在以什么速度发展呢？大经济学家林毅夫教授预言中国的经济在2030年将赶上美国，这难道不是中国政策正确的标志吗？是谁希望我们停止经济发动机而陷入混乱之中？恐怕就是在经济上被我们追赶上或要追赶上的国家吧？假设两个人比武，一方如果完全效仿对方的招术，在战略上怎么可能超越对方？这就是中国在科技上难以超越西方国家的根本原因，因为我们总是亦步亦趋地在科技大国的后面进行研究，缺乏战略创新、行业引领的动力。因此，在相互对抗中，弱方只有运用与对方不同的战法才有机会超越对手。中国的经济状况已经表明中国的制度是成功的，是有利于经济发展的，凭什么我们一定要改换成西方的方式呢？（掌声）<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;再说说境外的民运分子。他们轻松地坐在家里，一心想的就是如何仅凭手指敲着键盘，就利用互联网的放大效应来搞乱中国。这就如同网络攻击中的反射式拒绝服务攻击一样，凭借的是网络的倍增效应来攻击目标（议论声）。他们所煽动的集会是要达到什么目的？真的是要诉求个人利益吗？显然不是，因为没有这么多人的个人情况是相同的。我支持个人利益诉求，这也是我公开我的邮箱的原因。我欢迎所有师生直接向我反映问题，因为有问题就应该谋求解决，至少我可以答复什么原因解决不了什么样的问题。但是，不同利益诉求的人聚集在一起会有什么样的共同语言？唯一的共同点就是将个人利益诉求演变成政治利益的诉求。问题是这样就能解决个人利益的诉求吗？最后还不是沦落成境外这些职业政客们的工具？他们不就是指望着享受国外的生活、让公众成为傀儡、然后坐收渔利吗？难道他们回国来主政就能够把中国的经济搞得更好吗？事实上，中国被西方世界所敌视绝不仅仅是意识形态的问题，而是中国在世界上地位日益上升所引发的问题。俄罗斯的政体倒是转换到西方的模式上去了，不是照样被西方世界所敌视吗？<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;一个国家的政体就如同一座大厦，难道仅仅因为水龙头修不好就要把整幢楼拆除吗？要知道拆掉一幢楼而去重新建设新楼其代价是极其高昂和惨烈的（议论声）。利比亚正在给我们示范着这样的结局，已经有三十余万人逃离了这个国家。既然我们要继续住在这个大厦里，我们就决不能允许任何人对这座大厦进行破坏！因此，爱国就是要爱护我们赖以生存的家园，抵制造谣蛊惑者让中国社会动乱的任何企图。抢盐事件已经给我们以这样的启示：如果大家都能抵制那些谣言与煽动、看透这些蛊惑背后的阴谋与险恶的嘴脸，社会才能够保持稳定。因此，真正的爱国之情就是要像保护自己眼球一样来维护社会的稳定。（掌声）<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;同学们，无论你们今后走到哪里、工作在什么岗位，都要一如既往地秉承“厚德、博学，敬业、乐群”的校训，弘扬“团结、勤奋、严谨、创新”的校风，你们所取得的每一项成绩，都是对祖国、对母校最好的支持与回报！我衷心祝愿每一位同学：常怀爱国之心，常抒爱国之情！健康快乐，前程似锦，鹏程万里！<br />&nbsp;<br />&nbsp;&nbsp; &nbsp;谢谢大家！（长时间掌声）<br /><br /><br />[i]美国、法国、英国、加拿大、挪威、比利时、卡塔尔、阿联酋','',10,3,0,'2011-04-07 16:55:11','2011-04-07 16:56:10',NULL,0),(12,'北京邮电大学新增1个一级学科博士、9个一级学科硕士和3个硕士专业学位授权点','2011年3月3日国务院学位委员会印发《关于下达2010年审核增列的博士和硕士学位授权一级学科名单的通知》（学位[2011]8号），我校在2010年自行审核增列的1个一级学科博士学位授权点和9个一级学科硕士学位授权点全部通过国务院学位委员会第二十八次会议审批。<br />&nbsp;&nbsp; 获批的一级学科博士学位授权点是：控制科学与工程；获批的一级学科硕士学位授权点包括：应用经济学、法学、马克思主义理论、外国语言文学、新闻传播学、数学、物理学、工商管理、公共管理。<br />&nbsp;&nbsp; 通过此次一级学科学位授权点的增列，我校现有一级学科博士学位授权点6个，一级学科硕士学位授权点18个（军队指挥学一级学科硕士授权点待军队学位委员会批准），另有2个二级学科博士点和4个二级学科硕士点。<br /><br /><br />今年我校还新增列了硕士专业学位授权点3个，它们是：翻译、公共管理、工程管理。<br />&nbsp;&nbsp; 通过新增的学科点的获批，使我校的学科结构和布局更加合理，拓宽了我校的学科、专业领域，充分发挥学科建设对我校教学科研和人才培养等方面的结构性支撑作用，把握学科调整的主动权，构建结构优化的学位授权体系等各方面工作都将起到重要的推动作用，全面提升学校的核心竞争力，努力加快我校具有行业特色的高水平研究型大学的建设步伐。','',10,4,0,'2011-04-07 16:58:34','2011-04-07 16:58:34',NULL,0),(13,'热烈祝贺依托我校的“信息光子学与光通信国家重点实验室”获准立项','&nbsp;&nbsp; &nbsp; &nbsp; &nbsp;科技部于2011年4月2日在其网站上公布了《关于制定国家重点实验室建设计划的通知》（国科办基 [2011] 20号）。全国共有49个新的国家重点实验室获准立项，依托我校的“信息光子学与光通信国家重点实验室”为其中之一。这是我校拥有的第二个国家重点实验室；这是原同名教育部重点实验室（以下简称“实验室”）全体师生在科技部和教育部的关怀与指导下，在校领导、校内相关职能部门、全校师生和学术界同行的大力支持下，坚持不懈、艰苦努力的结果；这一事件是我校重点学科建设和重点科研基地建设历史进程中又一块重要的里程碑，值得我们热烈庆贺！<br />　　实验室创始人为我校原名誉校长、实验室学术委员会原名誉主任、著名光通信与微波通信专家叶培大院士。<br />　　实验室的名誉主任为诺贝尔物理学奖获得者、俄罗斯科学院副院长阿尔费罗夫院士，主任为任晓敏教授；学术委员会主任为周炳琨院士。与实验室同名的信息光子学与光通信研究院是实验室的实体支撑机构，实验室与研究院实行一体化的运行机制。<br />　　实验室的历史可追溯到上世纪六十年代，1988年该实验室即成为邮电部重点实验室。随着政府机构调整，1998年成为信息产业部重点实验室，2003年起立项建设教育部重点实验室，2005年作为教育部重点实验室正式开放运行。2007年，经教育部推荐和科技部同意，实验室作为少数特许的部级重点实验室之一参加了科技部组织的信息领域国家重点实验室评估，评估结果为良好。<br />　　实验室定位为在光信息科学与技术学科领域主要从事应用基础研究的科技创新和人才培养基地。实验室主要依托“电子科学与技术” 国家一级重点学科（相应的二级学科为“电磁场与微波技术”和“物理电子学”），同时依托“信息与通信工程”国家一级重点学科（相应的二级学科为“通信与信息系统”）以及“光学工程”一级学科博士点，立足“信息光子学与光通信”研究领域 ,坚持基础探索和工程技术相辅相成、光子学与光通信 “驱”“牵”互动、光通信与光信息处理交叉融合的发展模式，应在为国家解决本领域重大科技问题方面起到不可替代的作用，并在国际同类高水平研究机构中以较为明显的特色占有重要的一席之地。<br />　　长期以来，在叶培大院士、徐大雄院士等老一代科学家的带领下，实验室形成了一支年龄结构和知识结构合理、学术思想活跃、创新精神强的研究团队和以室训“执着出奇，团结致胜”为代表的实验室文化与传统，为我国信息光子学与光通信事业的发展作出了重要的贡献。在光通信发展的各个不同历史阶段，实验室的研究成果均代表了我国在该领域的研究实力和学术水平。<br />　　本次新增国家重点实验室的遴选工作是科技部于2010年10月启动的。同年11月中旬，经教育部推荐，实验室向科技部正式报送了申请书；同年12月30日实验室通过了科技部组织的以电话答辩方式进行的初评，顺利进入复评阶段；2011年1月25日，实验室通过了科技部专家组的现场考察；1月27日，实验室又参加了复评工作的最后一个环节——集中会议答辩。此次申请工作凝聚了实验室全体师生的智慧和心血，得到了校党委书记王亚杰教授、校长方滨兴院士等校领导以及相关职能部门的高度重视，得到了全校师生的热忱鼓励和鼎力支持。这是一段紧张、激越而又令人难以忘怀的岁月。<br />　　“宝剑锋从磨砺出，梅花香自苦寒来。”今天，晋级国家重点实验室的梦想在历经20年的“风雨兼程”之后终于成为现实，叶培大先生等老一辈科学家夙愿已偿、功垂青史，一批中青年优秀人才肩负重任、继往开来，实验室的历史掀开了新的一页！<br />　　当天下午，我校副校长、实验室主任任晓敏教授，副主任顾畹仪教授、黄永清教授，校科研基地办王彦主任、信息光子学与光通信研究院副院长张杰教授以及实验室陈雪教授、伍剑教授、张民教授和校务办郝加全老师等一行9人前往八宝山革命公墓骨灰堂深情告慰了77天前刚刚仙逝的叶先生！<br />　　我们相信，叶先生开创的事业正在一个新的高度上得以发扬光大！信息光子学与光通信国家重点实验室必将在今后的科技创新和人才培养中取得更为突出的成果，继续谱写“与光同行”的辉煌！北邮在建设信息科技特色突出、工管文理协调发展的世界高水平研究型大学的道路上将迈出更为坚实的步伐。','',10,4,0,'2011-04-07 16:59:48','2011-04-07 16:59:48',NULL,0),(16,'保卫处组织“防诈骗”宣传活动','为提高我校师生安全意识和防范意识，4月11日上午保卫处在学校小松林组织“防诈骗”主题宣传活动。活动中保卫处通过发放“谨防电信诈骗”宣传单、展览“防诈骗”宣传板等形式，向师生们展示了诈骗的常见种类和手法，通过分析当前诈骗案件发生的形势，明确了诈骗案件的防范重点和应对措施。<br />本次“防诈骗”专题宣传活动共展出宣传展板5张、分发宣传单2000余份，受到了同学们的广泛欢迎。<br />此外，保卫处人员还通过现场讲解典型案例、现场答疑、现场互动等形式，积极引导学生掌握基本防范技巧和识别日常诈骗的技能，切实增强了我校学生防范电信诈骗犯罪的能力，取得了良好的宣传教育效果。','',10,15,0,'2011-04-13 14:49:55','2011-04-13 14:49:55',NULL,0);
/*!40000 ALTER TABLE `cms_article` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_category`
--

DROP TABLE IF EXISTS `cms_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `type` smallint(6) NOT NULL,
  `url` varchar(255) DEFAULT NULL,
  `created` datetime NOT NULL,
  `lastModified` datetime NOT NULL,
  `father_id` int(11) DEFAULT NULL,
  `appLabel` varchar(30) DEFAULT NULL,
  `description` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `father_id_refs_id_80778eb9` (`father_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_category`
--

LOCK TABLES `cms_category` WRITE;
/*!40000 ALTER TABLE `cms_category` DISABLE KEYS */;
INSERT INTO `cms_category` VALUES (6,'班车信息','icon/2011/090/hours.png',40,NULL,'2011-03-31 14:01:35','2011-03-31 14:01:35',NULL,'bus_info_cn',''),(7,'安保信息','icon/2011/090/emergency.png',10,NULL,'2011-03-31 14:02:05','2011-04-13 14:37:45',NULL,'security_info_cn',''),(8,'绿色校园','',30,NULL,'2011-03-31 14:10:26','2011-03-31 14:10:26',5,'',''),(2,'快速通道','icon/2011/079/links.png',50,NULL,'2011-03-20 20:41:28','2011-03-31 14:00:31',NULL,'fast_track_cn',''),(3,'校长演讲','icon/2011/079/directory.png',20,NULL,'2011-03-20 21:08:55','2011-03-31 14:11:03',5,'',''),(4,'北邮新闻','icon/2011/090/edu.png',20,NULL,'2011-03-31 13:57:30','2011-03-31 13:57:30',NULL,'bupt_news_cn',''),(5,'学校概况','icon/2011/103/libraries.png',10,NULL,'2011-03-31 13:59:09','2011-04-13 14:13:29',NULL,'school_info_cn',''),(9,'名师大家','',30,NULL,'2011-03-31 14:12:16','2011-03-31 14:12:16',5,'',''),(10,'领导机构','',40,NULL,'2011-03-31 14:12:44','2011-03-31 14:12:44',5,'',''),(11,'历史沿革','',40,NULL,'2011-03-31 14:13:14','2011-03-31 14:13:14',5,'',''),(12,'学校简介','',40,NULL,'2011-03-31 14:13:42','2011-03-31 14:13:42',5,'',''),(13,'北邮人','icon/2011/103/directory.png',70,'http://forum.byr.edu.cn/rss/board-Focus','2011-04-13 14:14:31','2011-04-13 14:14:31',NULL,'byr',''),(14,'警情提示','',20,NULL,'2011-04-13 14:38:48','2011-04-13 14:42:50',7,'',''),(15,'宣教活动','',20,NULL,'2011-04-13 14:46:13','2011-04-13 14:46:13',7,'','');
/*!40000 ALTER TABLE `cms_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments_building`
--

DROP TABLE IF EXISTS `departments_building`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments_building` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` longtext,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments_building`
--

LOCK TABLES `departments_building` WRITE;
/*!40000 ALTER TABLE `departments_building` DISABLE KEYS */;
INSERT INTO `departments_building` VALUES (1,'行政楼','校办、人事处、学生处',39.96246,116.356802),(2,'教一楼','教学、工会、外语',39.96246,116.356802),(0,'北京邮电大学','北京市海淀区西土城路10号',39.96246,116.356802),(4,'教一楼旁','财务处、资产处',39.96246,116.356802),(5,'西校门保卫处','保卫处',39.76246,116.356802),(6,'学生八公寓','住宿',39.96246,116.356802);
/*!40000 ALTER TABLE `departments_building` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments_department`
--

DROP TABLE IF EXISTS `departments_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `description` longtext,
  `room` varchar(8) DEFAULT NULL,
  `telephone` varchar(12) DEFAULT NULL,
  `worktime` varchar(50) DEFAULT NULL,
  `website` varchar(200) DEFAULT NULL,
  `building_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `departments_department_57000c84` (`building_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments_department`
--

LOCK TABLES `departments_department` WRITE;
/*!40000 ALTER TABLE `departments_department` DISABLE KEYS */;
INSERT INTO `departments_department` VALUES (1,'校务办公室','学校拥有雄厚的师资力量，通信高技术教育教学与研究的整体实力处于国内领先地位。在2001年全国重点学科评定中，学校的4个核心学科均排在全国高校的前5名。学校拥有1个国家重点实验室、2个国家工程研究中心和8个省、部级设置的研究（院、所、中心）、实验室，以及2个国家一级重点学科和13个省、部重点学科。','408','62282044','上午8:30到11:30,下午1:30到5:00','http://xwb.bupt.edu.cn/',1),(2,'人事处','（1）职务分析与设计。对企业各个工作职位的性质、结构、责任、流程，以及胜任该职位工作人员的素质，知识、技能等，在调查分析所获取相关信息的基础上，编写出职务说明书和岗位规范等人事管理文件。\r\n\r\n（2）人力资源规划。把企业人力资源战略转化为中长期目标、计划和政策措施，包括对人力资源现状分析、未来人员供需予测与平衡，确保企业在需要时能获得所需要的人力资源。\r\n\r\n（3）员工招聘与选拔。根据人力资源规划和工作分析的要求，为企业招聘、选拔所需要人力资源并录用安排到一定岗位上。\r\n\r\n（4）绩效考评。对员工在一定时间内对企业的贡献和工作中取得的绩效进行考核和评价，及时做出反馈，以便提高和改善员工的工作绩效，并为员工培训、晋升、计酬等人事决策提供依据。','201','622822165','上午8:30到11:30,下午1:30到5:00','http://rsc.bupt.edu.cn/',1),(3,'财务处','财务处设5个科，预算管理科、会计核算科、资金结算科、会计事务科、专项资金科。\r\n财务处设岗位30个，其中含处长岗位1个、副处长岗位2个、科长岗位5个、副科长岗位1个、科员岗位21个。','110','62283797','上午8:30到11:30,下午1:30到5:00','http://cwc.bupt.edu.cn/',4),(4,'科技处','负责科技处信息管理平台、科技处主页的维护和管理；负责科技综合统计和科技经费的拨款；管理国家科技重大专项项目、国家科技支撑计划项目、工信部渠道项目和标准研究项目等。','505','62282042','上午8:30到11:30,下午1:30到5:00','http://kjc.bupt.edu.cn/',2),(5,'保卫处','负责学校政治保卫和国家安全工作，做好校内重大外事活动和大型活动以及节、假日的安全防范工作。\r\n负责校防火安全委员会的办公室工作，按照《中华人民共和国消防法》认真检查落实学校的防火安全和隐患整改工作。\r\n负责学校保密委员会和交通安全委员会办公室的日常工作。\r\n负责校治安综合治理委员会的办公室日常工作，落实校治安综合治理委员会会议决议，检查各单位贯彻《北京邮电大学治安综合治理责任制》的落实情况。\r\n','202','62282774','上午8:30到11:30,下午1:30到5:00','http://bwc.bupt.edu.cn/',5),(6,'学生处','北京邮电大学学生处是在校党、政领导下，学生事务管理处、党委学生工作部及武装部合署办公的学生管理机构，负责全校本科生及研究生的教育管理工作。\r\n    具体机构包括思想教育科、学生管理科、助学中心、心理健康教育中心、公寓中心、军事教研室及四个辅导员管理科。','205','62282736','上午8:30到11:30,下午1:30到5:00','http://xsc.bupt.edu.cn/',1);
/*!40000 ALTER TABLE `departments_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments_subdepartment`
--

DROP TABLE IF EXISTS `departments_subdepartment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments_subdepartment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `room` varchar(8) DEFAULT NULL,
  `telephone` varchar(12) DEFAULT NULL,
  `building_id` int(11) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `departments_subdepartment_57000c84` (`building_id`),
  KEY `departments_subdepartment_2ae7390` (`department_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments_subdepartment`
--

LOCK TABLES `departments_subdepartment` WRITE;
/*!40000 ALTER TABLE `departments_subdepartment` DISABLE KEYS */;
INSERT INTO `departments_subdepartment` VALUES (1,'机要科','404','62282239',1,1),(2,'综合科','308','62282044',1,1),(3,'劳 资 科','206','62282602',1,2),(4,'人 事 科','204','62282646',1,2);
/*!40000 ALTER TABLE `departments_subdepartment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2011-04-13 17:20:04',1,13,'1','小白楼',1,''),(2,'2011-04-13 17:20:13',1,13,'1','小白楼',2,'没有字段被修改。'),(3,'2011-04-13 17:21:19',1,13,'2','教一楼',1,''),(4,'2011-04-13 17:22:04',1,14,'1','校办',1,''),(5,'2011-04-13 17:23:27',1,15,'1','保密科',1,''),(6,'2011-04-13 17:32:54',1,13,'0','北京邮电大学',2,'已修改 name, description, latitude 和 longitude 。'),(7,'2011-04-13 17:46:01',1,14,'2','人事处',1,''),(8,'2011-04-13 17:50:04',1,13,'4','教一楼旁',1,''),(9,'2011-04-13 17:50:28',1,14,'3','财务处',1,''),(10,'2011-04-13 17:50:44',1,14,'3','财务处',2,'Changed building.'),(11,'2011-04-13 17:54:26',1,14,'1','校务办公室',2,'已修改 name 和 website 。'),(12,'2011-04-13 17:55:27',1,13,'1','行政楼',2,'已修改 name 和 description 。'),(13,'2011-04-13 17:56:27',1,14,'1','校务办公室',2,'已修改 telephone 。'),(14,'2011-04-13 17:57:04',1,14,'1','校务办公室',2,'已修改 room 。'),(15,'2011-04-13 17:58:32',1,15,'2','综合科',1,''),(16,'2011-04-13 18:00:52',1,15,'3','劳 资 科',1,''),(17,'2011-04-13 18:02:39',1,15,'4','人 事 科',1,''),(18,'2011-04-13 18:03:02',1,15,'3','劳 资 科',2,'已修改 telephone 。'),(19,'2011-04-13 18:04:08',1,15,'1','机要科',2,'已修改 name 和 telephone 。'),(20,'2011-04-13 18:06:45',1,14,'4','科技处',1,''),(21,'2011-04-13 18:11:24',1,13,'5','西校门保卫处',1,''),(22,'2011-04-13 18:11:39',1,14,'5','保卫处',1,''),(23,'2011-04-13 18:11:51',1,14,'5','保卫处',2,'已修改 building 。'),(24,'2011-04-13 18:15:05',1,14,'1','校务办公室',2,'已修改 description 。'),(25,'2011-04-13 18:16:03',1,14,'3','财务处',2,'已修改 description 。'),(26,'2011-04-13 21:04:46',1,11,'4','4',2,'没有字段被修改。'),(27,'2011-04-13 21:51:03',1,13,'6','学生八公寓',1,''),(28,'2011-04-13 21:53:56',1,14,'6','学生处',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(9,'Category','cms','category'),(10,'Article','cms','article'),(11,'Feedback','feedback','feedback'),(12,'Feature Suggest','feedback','suggestfeature'),(13,'building','departments','building'),(14,'department','departments','department'),(15,'sub department','departments','subdepartment');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('80ee5c400c7b01754ba315ba8f501e77','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS45MzdlZmE2NWE1ZmJkY2YzYzlm\nZTczNTM0ZTY1Y2RiYg==\n','2011-04-03 20:18:12'),('a8c34d05bbd88d18f879b639dab481c9','gAJ9cQEuNjJiZDA5ZDc0ODAxZmE3NDY4MmM5NmMxYmE0MjllY2I=\n','2011-04-23 23:23:23'),('62d374f3edb0215ef21eb162034ed878','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS45MzdlZmE2NWE1ZmJkY2YzYzlm\nZTczNTM0ZTY1Y2RiYg==\n','2011-04-27 20:17:12'),('e4236c864bfd6023003e4d786ca0d829','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS45MzdlZmE2NWE1ZmJkY2YzYzlm\nZTczNTM0ZTY1Y2RiYg==\n','2011-04-21 16:20:22'),('61a9eeb02ebf0d6e08ec17c814091a42','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UPZGphbmdvX2xhbmd1YWdlcQRYBQAAAHpoLWNucQVVDV9hdXRoX3Vz\nZXJfaWRxBooBAXUuN2Q2NDE5ZDg5YmIxMzM4MzU3ZDkyNDg3MTZhOTMzZGU=\n','2011-04-24 18:30:39'),('e71225c0a37845420cf9bafd0e977765','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS45MzdlZmE2NWE1ZmJkY2YzYzlm\nZTczNTM0ZTY1Y2RiYg==\n','2011-04-25 20:57:34'),('eb142ba75bee58481c0af6031ae2da58','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS45MzdlZmE2NWE1ZmJkY2YzYzlm\nZTczNTM0ZTY1Y2RiYg==\n','2011-04-25 12:35:46'),('c38d664343360872a76a722979fa0052','gAJ9cQEuNjJiZDA5ZDc0ODAxZmE3NDY4MmM5NmMxYmE0MjllY2I=\n','2011-04-26 18:48:27'),('779a1a1de7a9c127f3d33e0495c3f47c','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UNX2F1dGhfdXNlcl9pZHEEigEBdS45MzdlZmE2NWE1ZmJkY2YzYzlm\nZTczNTM0ZTY1Y2RiYg==\n','2011-04-28 15:51:23'),('577219e73ffcef69013424b048234e8e','gAJ9cQEoVRJfYXV0aF91c2VyX2JhY2tlbmRxAlUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5k\ncy5Nb2RlbEJhY2tlbmRxA1UPZGphbmdvX2xhbmd1YWdlcQRYBQAAAHpoLWNucQVVDV9hdXRoX3Vz\nZXJfaWRxBooBAXUuN2Q2NDE5ZDg5YmIxMzM4MzU3ZDkyNDg3MTZhOTMzZGU=\n','2011-04-28 08:53:19'),('90d3e627f64b00286e8fa19ba5a98aec','gAJ9cQFVCnRlc3Rjb29raWVxAlUGd29ya2VkcQNzLmEyOGZkOTcxZmIwMjg4ZDdmMmIwN2FjMzhh\nYzM2Mjll\n','2011-04-27 22:08:20'),('ec02212c4435dc0464a81edf080c13cd','gAJ9cQEoVQp0ZXN0Y29va2llcQJVBndvcmtlZHEDVQ9kamFuZ29fbGFuZ3VhZ2VxBFgFAAAAemgt\nY25xBXUuNWZiMDJkYTdjNDY4ZTdmMzQzNGM5NTNiZDg3MzNjNDk=\n','2011-05-01 16:35:03');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_feedback`
--

DROP TABLE IF EXISTS `feedback_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(75) DEFAULT NULL,
  `referer` varchar(255) DEFAULT NULL,
  `content` longtext NOT NULL,
  `read` tinyint(1) NOT NULL,
  `commited` datetime NOT NULL,
  `commitedIp` char(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_feedback`
--

LOCK TABLES `feedback_feedback` WRITE;
/*!40000 ALTER TABLE `feedback_feedback` DISABLE KEYS */;
INSERT INTO `feedback_feedback` VALUES (1,'','http://exp.nesdu.org/weather/','使用中国移动的网络访问速度比较慢。',0,'2011-04-10 18:33:48','59.64.176.28'),(2,'','http://exp.nesdu.org/content/2/','速度有点慢',0,'2011-04-11 10:46:41','59.64.176.252'),(3,'','http://exp.nesdu.org/content/2/#home','用联通的网络访问比较慢',0,'2011-04-12 11:56:46','59.64.176.252'),(4,'','http://exp.nesdu.org/content/2/#home','用联通的网络访问比较慢',0,'2011-04-12 11:56:46','59.64.176.252');
/*!40000 ALTER TABLE `feedback_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_suggestfeature`
--

DROP TABLE IF EXISTS `feedback_suggestfeature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_suggestfeature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(75) DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `content` longtext NOT NULL,
  `read` tinyint(1) NOT NULL,
  `commited` datetime NOT NULL,
  `commitedIp` char(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_suggestfeature`
--

LOCK TABLES `feedback_suggestfeature` WRITE;
/*!40000 ALTER TABLE `feedback_suggestfeature` DISABLE KEYS */;
/*!40000 ALTER TABLE `feedback_suggestfeature` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-04-21 20:30:28
