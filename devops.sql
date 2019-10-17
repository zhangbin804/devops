-- MySQL dump 10.14  Distrib 5.5.60-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: devops
-- ------------------------------------------------------
-- Server version	5.6.40-log

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
-- Table structure for table `accounts_navigation`
--

DROP TABLE IF EXISTS `accounts_navigation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_navigation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `website_name` varchar(32) NOT NULL,
  `website_url` varchar(256) NOT NULL,
  `name_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_navigation_name_id_8b74c2f5_fk_permissions_user_id` (`name_id`),
  CONSTRAINT `accounts_navigation_name_id_8b74c2f5_fk_permissions_user_id` FOREIGN KEY (`name_id`) REFERENCES `permissions_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_navigation`
--

LOCK TABLES `accounts_navigation` WRITE;
/*!40000 ALTER TABLE `accounts_navigation` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_navigation` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add intermediate',7,'add_intermediate'),(26,'Can change intermediate',7,'change_intermediate'),(27,'Can delete intermediate',7,'delete_intermediate'),(28,'Can view intermediate',7,'view_intermediate'),(29,'Can add process',8,'add_process'),(30,'Can change process',8,'change_process'),(31,'Can delete process',8,'delete_process'),(32,'Can view process',8,'view_process'),(33,'Can add navigation',9,'add_navigation'),(34,'Can change navigation',9,'change_navigation'),(35,'Can delete navigation',9,'delete_navigation'),(36,'Can view navigation',9,'view_navigation'),(37,'Can add group',10,'add_group'),(38,'Can change group',10,'change_group'),(39,'Can delete group',10,'delete_group'),(40,'Can view group',10,'view_group'),(41,'Can add menu',11,'add_menu'),(42,'Can change menu',11,'change_menu'),(43,'Can delete menu',11,'delete_menu'),(44,'Can view menu',11,'view_menu'),(45,'Can add permission',12,'add_permission'),(46,'Can change permission',12,'change_permission'),(47,'Can delete permission',12,'delete_permission'),(48,'Can view permission',12,'view_permission'),(49,'Can add role',13,'add_role'),(50,'Can change role',13,'change_role'),(51,'Can delete role',13,'delete_role'),(52,'Can view role',13,'view_role'),(53,'Can add user',14,'add_user'),(54,'Can change user',14,'change_user'),(55,'Can delete user',14,'delete_user'),(56,'Can view user',14,'view_user'),(57,'Can add group',15,'add_group'),(58,'Can change group',15,'change_group'),(59,'Can delete group',15,'delete_group'),(60,'Can view group',15,'view_group'),(61,'Can add server',16,'add_server'),(62,'Can change server',16,'change_server'),(63,'Can delete server',16,'delete_server'),(64,'Can view server',16,'view_server'),(65,'Can add server user',17,'add_serveruser'),(66,'Can change server user',17,'change_serveruser'),(67,'Can delete server user',17,'delete_serveruser'),(68,'Can view server user',17,'view_serveruser'),(69,'Can add log',18,'add_log'),(70,'Can change log',18,'change_log'),(71,'Can delete log',18,'delete_log'),(72,'Can view log',18,'view_log'),(73,'Can add project',19,'add_project'),(74,'Can change project',19,'change_project'),(75,'Can delete project',19,'delete_project'),(76,'Can view project',19,'view_project');
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
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$120000$c6dL18uzGx5u$w9ACHbGmzX7Ix3EWno69rm0/6j95OSrI/ccU0HBNUQc=','2019-10-16 08:20:13.649129',1,'admin','','','',1,1,'2019-10-16 08:19:52.425952');
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
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
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
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-10-16 08:33:47.741607','1','网站导航',1,'[{\"added\": {}}]',11,1),(2,'2019-10-16 08:34:00.974465','2','流程控制',1,'[{\"added\": {}}]',11,1),(3,'2019-10-16 08:34:11.597099','3','运维工具',1,'[{\"added\": {}}]',11,1),(4,'2019-10-16 08:34:23.497310','4','系统设置',1,'[{\"added\": {}}]',11,1),(5,'2019-10-16 08:34:35.857450','5','项目管理',1,'[{\"added\": {}}]',11,1),(6,'2019-10-16 08:34:54.456476','6','权限管理',1,'[{\"added\": {}}]',11,1),(7,'2019-10-16 08:37:26.515192','1','project',1,'[{\"added\": {}}]',10,1),(8,'2019-10-16 08:37:50.388625','2','process',1,'[{\"added\": {}}]',10,1),(9,'2019-10-16 08:38:01.370429','2','流程管理',2,'[{\"changed\": {\"fields\": [\"caption\"]}}]',11,1),(10,'2019-10-16 08:38:18.918462','3','permissions',1,'[{\"added\": {}}]',10,1),(11,'2019-10-16 08:38:30.085386','4','operational',1,'[{\"added\": {}}]',10,1),(12,'2019-10-16 08:38:43.494228','5','configuration',1,'[{\"added\": {}}]',10,1),(13,'2019-10-16 08:39:20.233686','6','website',1,'[{\"added\": {}}]',10,1),(14,'2019-10-16 08:42:55.412767','1','添加导航',1,'[{\"added\": {}}]',12,1),(15,'2019-10-16 08:43:59.566441','2','删除导航',1,'[{\"added\": {}}]',12,1),(16,'2019-10-16 08:46:08.443675','3','修改邮箱',1,'[{\"added\": {}}]',12,1),(17,'2019-10-16 08:46:55.313571','4','修改密码',1,'[{\"added\": {}}]',12,1),(18,'2019-10-16 08:47:17.937065','5','修改头像',1,'[{\"added\": {}}]',12,1),(19,'2019-10-16 08:54:56.062699','6','服务器管理列表',1,'[{\"added\": {}}]',12,1),(20,'2019-10-16 08:57:04.805762','7','查看服务器',1,'[{\"added\": {}}]',12,1),(21,'2019-10-16 08:57:41.246519','8','编辑服务器',1,'[{\"added\": {}}]',12,1),(22,'2019-10-16 09:05:47.015693','9','删除服务器',1,'[{\"added\": {}}]',12,1),(23,'2019-10-16 09:06:13.425263','10','服务器组列表',1,'[{\"added\": {}}]',12,1),(24,'2019-10-16 09:07:12.789149','11','添加服务器',1,'[{\"added\": {}}]',12,1),(25,'2019-10-16 09:07:53.460095','12','添加服务器组',1,'[{\"added\": {}}]',12,1),(26,'2019-10-16 09:08:18.544534','13','删除服务器组',1,'[{\"added\": {}}]',12,1),(27,'2019-10-16 09:09:12.182935','14','修改服务器组',1,'[{\"added\": {}}]',12,1),(28,'2019-10-16 09:09:53.442429','15','查看服务器组',1,'[{\"added\": {}}]',12,1),(29,'2019-10-16 09:11:17.407772','16','随机密码',1,'[{\"added\": {}}]',12,1),(30,'2019-10-16 09:11:54.979530','17','ssh账号列表',1,'[{\"added\": {}}]',12,1),(31,'2019-10-16 09:12:29.019422','18','添加ssh账号',1,'[{\"added\": {}}]',12,1),(32,'2019-10-16 09:13:01.073400','19','删除ssh账号',1,'[{\"added\": {}}]',12,1),(33,'2019-10-16 09:13:41.606318','20','修改ssh账号',1,'[{\"added\": {}}]',12,1),(34,'2019-10-16 09:14:02.499711','21','查看ssh账号',1,'[{\"added\": {}}]',12,1),(35,'2019-10-16 09:15:11.899831','22','权限管理列表',1,'[{\"added\": {}}]',12,1),(36,'2019-10-16 09:16:01.490184','23','添加账号',1,'[{\"added\": {}}]',12,1),(37,'2019-10-16 09:16:48.417175','24','删除账号',1,'[{\"added\": {}}]',12,1),(38,'2019-10-16 09:19:41.244052','25','修改账号',1,'[{\"added\": {}}]',12,1),(39,'2019-10-16 09:20:47.959003','26','账号列表',1,'[{\"added\": {}}]',12,1),(40,'2019-10-16 09:21:28.940206','27','启用与禁用账号',1,'[{\"added\": {}}]',12,1),(41,'2019-10-16 09:22:53.589687','28','更改权限',1,'[{\"added\": {}}]',12,1),(42,'2019-10-16 09:23:57.690120','29','权限修改列表',1,'[{\"added\": {}}]',12,1),(43,'2019-10-17 02:32:07.022663','30','更改权限',1,'[{\"added\": {}}]',12,1),(44,'2019-10-17 02:32:58.362988','30','更改权限',3,'',12,1),(45,'2019-10-17 02:34:03.051844','31','添加角色组',1,'[{\"added\": {}}]',12,1),(46,'2019-10-17 02:34:28.482453','32','删除角色组',1,'[{\"added\": {}}]',12,1),(47,'2019-10-17 02:36:03.357360','33','流程列表',1,'[{\"added\": {}}]',12,1),(48,'2019-10-17 02:36:49.746614','34','添加流程表',1,'[{\"added\": {}}]',12,1),(49,'2019-10-17 02:37:38.913787','35','删除流程表',1,'[{\"added\": {}}]',12,1),(50,'2019-10-17 02:38:35.420795','36','编辑流程表',1,'[{\"added\": {}}]',12,1),(51,'2019-10-17 02:40:02.318504','37','更改流程表',1,'[{\"added\": {}}]',12,1),(52,'2019-10-17 02:40:42.672543','38','查看流程表',1,'[{\"added\": {}}]',12,1),(53,'2019-10-17 02:41:36.690704','39','创建流程',1,'[{\"added\": {}}]',12,1),(54,'2019-10-17 02:42:23.252212','40','所有流程记录',1,'[{\"added\": {}}]',12,1),(55,'2019-10-17 02:42:49.485034','41','流程审核列表',1,'[{\"added\": {}}]',12,1),(56,'2019-10-17 02:46:36.171255','42','审核流程',1,'[{\"added\": {}}]',12,1),(57,'2019-10-17 02:47:45.725340','43','项目管理列表',1,'[{\"added\": {}}]',12,1),(58,'2019-10-17 02:48:11.393071','44','添加项目',1,'[{\"added\": {}}]',12,1),(59,'2019-10-17 02:48:46.784232','45','删除项目',1,'[{\"added\": {}}]',12,1),(60,'2019-10-17 02:49:10.433477','46','修改项目',1,'[{\"added\": {}}]',12,1),(61,'2019-10-17 02:49:37.626364','47','查看项目',1,'[{\"added\": {}}]',12,1),(62,'2019-10-17 02:50:08.605942','48','连接测试',1,'[{\"added\": {}}]',12,1),(63,'2019-10-17 02:50:57.148561','49','发布更新项目',1,'[{\"added\": {}}]',12,1),(64,'2019-10-17 02:51:36.132696','50','获取tag标签',1,'[{\"added\": {}}]',12,1),(65,'2019-10-17 02:52:05.792746','51','回滚项目',1,'[{\"added\": {}}]',12,1),(66,'2019-10-17 02:52:35.122640','1','管理员',1,'[{\"added\": {}}]',13,1),(67,'2019-10-17 02:57:50.684712','1','admin',1,'[{\"added\": {}}]',14,1);
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
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (9,'accounts','navigation'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(15,'operational','group'),(16,'operational','server'),(17,'operational','serveruser'),(10,'permissions','group'),(11,'permissions','menu'),(12,'permissions','permission'),(13,'permissions','role'),(14,'permissions','user'),(7,'process','intermediate'),(8,'process','process'),(18,'project','log'),(19,'project','project'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'permissions','0001_initial','2019-10-16 08:07:23.227667'),(2,'accounts','0001_initial','2019-10-16 08:07:23.579035'),(3,'contenttypes','0001_initial','2019-10-16 08:07:23.776412'),(4,'auth','0001_initial','2019-10-16 08:07:26.363452'),(5,'admin','0001_initial','2019-10-16 08:07:26.667690'),(6,'admin','0002_logentry_remove_auto_add','2019-10-16 08:07:26.693986'),(7,'admin','0003_logentry_add_action_flag_choices','2019-10-16 08:07:26.721832'),(8,'contenttypes','0002_remove_content_type_name','2019-10-16 08:07:26.863118'),(9,'auth','0002_alter_permission_name_max_length','2019-10-16 08:07:26.946572'),(10,'auth','0003_alter_user_email_max_length','2019-10-16 08:07:27.065705'),(11,'auth','0004_alter_user_username_opts','2019-10-16 08:07:27.076715'),(12,'auth','0005_alter_user_last_login_null','2019-10-16 08:07:27.188124'),(13,'auth','0006_require_contenttypes_0002','2019-10-16 08:07:27.191552'),(14,'auth','0007_alter_validators_add_error_messages','2019-10-16 08:07:27.219190'),(15,'auth','0008_alter_user_username_max_length','2019-10-16 08:07:27.384946'),(16,'auth','0009_alter_user_last_name_max_length','2019-10-16 08:07:27.489248'),(17,'operational','0001_initial','2019-10-16 08:07:28.580262'),(18,'process','0001_initial','2019-10-16 08:07:29.460027'),(19,'project','0001_initial','2019-10-16 08:07:30.129488'),(20,'sessions','0001_initial','2019-10-16 08:07:30.211795'),(21,'accounts','0002_auto_20191017_1056','2019-10-17 02:57:05.263441'),(22,'operational','0002_auto_20191017_1056','2019-10-17 02:57:05.354383'),(23,'permissions','0002_auto_20191017_1056','2019-10-17 02:57:05.397857'),(24,'process','0002_auto_20191017_1056','2019-10-17 02:57:05.443656'),(25,'project','0002_auto_20191017_1056','2019-10-17 02:57:05.561551'),(26,'permissions','0003_auto_20191017_1059','2019-10-17 02:59:29.036734');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('jn2kms2fsxa9uv4h5ckd9w84miq4svht','YjlhYTAyZmIzZWVjOWJiNTljM2Q4ZjlmZTg5YTkwYjU2YTU3OTYxZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzYTEzYjllM2Y4YTMzYzQ0ZjBiMDAyN2Y2NzRmYWZmYzAzZDgwYmRmIiwicGVybWlzc2lvbl91cmxfbGlzdCI6eyI2Ijp7ImNvZGUiOlsiMSIsIjEiXSwidXJscyI6WyIvYWRkL25hdmlnYXRpb24vIiwiL2RlbGV0ZS9uYXZpZ2F0aW9uLyJdfSwiNSI6eyJjb2RlIjpbIjQiLCI0IiwiNCJdLCJ1cmxzIjpbIi9jb25maWd1cmF0aW9uL2VkaXQvZW1haWwvIiwiL2NvbmZpZ3VyYXRpb24vZWRpdC9wYXNzd29yZC8iLCIvY29uZmlndXJhdGlvbi9lZGl0L2F2YXRhci8iXX0sIjQiOnsiY29kZSI6WyIzIiwiMyIsIjMiLCIzIiwiMyIsIjMiLCIzIiwiMyIsIjMiLCIzIiwiMyIsIjMiLCIzIiwiMyIsIjMiLCIzIl0sInVybHMiOlsiL29wZXJhdGlvbmFsL2xpc3Qvc2VydmVyLyIsIi9vcGVyYXRpb25hbC9yZWFkL3NlcnZlci8oWzAtOV0rKS8iLCIvb3BlcmF0aW9uYWwvZWRpdC9zZXJ2ZXIvKFswLTldKykvIiwiL29wZXJhdGlvbmFsL2RlbGV0ZS9zZXJ2ZXIvIiwiL29wZXJhdGlvbmFsL2xpc3QvZ3JvdXAvIiwiL29wZXJhdGlvbmFsL2NyZWF0ZS9zZXJ2ZXIvIiwiL29wZXJhdGlvbmFsL2NyZWF0ZS9ncm91cC8iLCIvb3BlcmF0aW9uYWwvZGVsZXRlL2dyb3VwLyIsIi9vcGVyYXRpb25hbC9lZGl0L2dyb3VwLyhbMC05XSspLyIsIi9vcGVyYXRpb25hbC9yZWFkL2dyb3VwLyhbMC05XSspLyIsIi9vcGVyYXRpb25hbC9jcmVhdGUvcGFzc3dvcmQvIiwiL29wZXJhdGlvbmFsL3NlcnZlci9saXN0L3VzZXIvIiwiL29wZXJhdGlvbmFsL3NlcnZlci9jcmVhdGUvdXNlci8iLCIvb3BlcmF0aW9uYWwvc2VydmVyL2RlbGV0ZS91c2VyLyIsIi9vcGVyYXRpb25hbC9zZXJ2ZXIvZWRpdC91c2VyLyIsIi9vcGVyYXRpb25hbC9zZXJ2ZXIvcmVhZC91c2VyLyJdfSwiMyI6eyJjb2RlIjpbIjYiLCI2IiwiNiIsIjYiLCI2IiwiNiIsIjYiLCI2IiwiNiIsIjYiXSwidXJscyI6WyIvcGVybWlzc2lvbnMvbGlzdC8iLCIvcGVybWlzc2lvbnMvY3JlYXRlL3VzZXIvIiwiL3Blcm1pc3Npb25zL2RlbGV0ZS91c2VyLyIsIi9wZXJtaXNzaW9ucy9lZGl0L3VzZXIvKFswLTldKykvIiwiL3Blcm1pc3Npb25zL2xpc3QvdXNlci8iLCIvcGVybWlzc2lvbnMvZGlzYWJsZS91c2VyLyIsIi9wZXJtaXNzaW9ucy9jaGFuZ2UvcGVybWlzc2lvbnMvIiwiL3Blcm1pc3Npb25zL2VkaXQvKFswLTldKykvIiwiL3Blcm1pc3Npb25zL2NyZWF0ZS9yb2xlcy8iLCIvcGVybWlzc2lvbnMvZGVsZXRlL3JvbGVzLyJdfSwiMiI6eyJjb2RlIjpbIjIiLCIyIiwiMiIsIjIiLCIyIiwiMiIsIjIiLCIyIiwiMiIsIjIiXSwidXJscyI6WyIvcHJvY2Vzcy9saXN0LyIsIi9wcm9jZXNzL2FkZC8iLCIvcHJvY2Vzcy9kZWxldGUvIiwiL3Byb2Nlc3MvZWRpdC8oWzAtOV0rKS8iLCIvcHJvY2Vzcy9zYXZlLyIsIi9wcm9jZXNzL2luZm8vKFswLTldKykvIiwiL3Byb2Nlc3MvY3JlYXRlLyIsIi9wcm9jZXNzL2FsbC8iLCIvcHJvY2Vzcy9hdWRpdC9saXN0LyIsIi9wcm9jZXNzL2F1ZGl0L2F1dGgvIl19LCIxIjp7ImNvZGUiOlsiNSIsIjUiLCI1IiwiNSIsIjUiLCI1IiwiNSIsIjUiLCI1Il0sInVybHMiOlsiL3Byb2plY3QvbGlzdC8iLCIvcHJvamVjdC9jcmVhdGUvIiwiL3Byb2plY3QvZGVsZXRlLyIsIi9wcm9qZWN0L2VkaXQvIiwiL3Byb2plY3QvcmVhZC8iLCIvcHJvamVjdC9jb25uZWN0aW9uL3Rlc3QvIiwiL3Byb2plY3QvcmVsZWFzZS8iLCIvcHJvamVjdC90YWcvIiwiL3Byb2plY3Qvcm9sbGJhY2svIl19fSwicGVybWlzc2lvbl9tZW51X2xpc3QiOlt7ImlkIjoxLCJ0aXRsZSI6Ilx1NmRmYlx1NTJhMFx1NWJmY1x1ODIyYSIsInVybCI6Ii9hZGQvbmF2aWdhdGlvbi8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjoxLCJtZW51X3RpdGxlIjoiXHU3ZjUxXHU3YWQ5XHU1YmZjXHU4MjJhIn0seyJpZCI6MiwidGl0bGUiOiJcdTUyMjBcdTk2NjRcdTViZmNcdTgyMmEiLCJ1cmwiOiIvZGVsZXRlL25hdmlnYXRpb24vIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MSwibWVudV90aXRsZSI6Ilx1N2Y1MVx1N2FkOVx1NWJmY1x1ODIyYSJ9LHsiaWQiOjMsInRpdGxlIjoiXHU0ZmVlXHU2NTM5XHU5MGFlXHU3YmIxIiwidXJsIjoiL2NvbmZpZ3VyYXRpb24vZWRpdC9lbWFpbC8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjo0LCJtZW51X3RpdGxlIjoiXHU3Y2ZiXHU3ZWRmXHU4YmJlXHU3ZjZlIn0seyJpZCI6NCwidGl0bGUiOiJcdTRmZWVcdTY1MzlcdTViYzZcdTc4MDEiLCJ1cmwiOiIvY29uZmlndXJhdGlvbi9lZGl0L3Bhc3N3b3JkLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjQsIm1lbnVfdGl0bGUiOiJcdTdjZmJcdTdlZGZcdThiYmVcdTdmNmUifSx7ImlkIjo1LCJ0aXRsZSI6Ilx1NGZlZVx1NjUzOVx1NTkzNFx1NTBjZiIsInVybCI6Ii9jb25maWd1cmF0aW9uL2VkaXQvYXZhdGFyLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjQsIm1lbnVfdGl0bGUiOiJcdTdjZmJcdTdlZGZcdThiYmVcdTdmNmUifSx7ImlkIjo2LCJ0aXRsZSI6Ilx1NjcwZFx1NTJhMVx1NTY2OFx1N2JhMVx1NzQwNlx1NTIxN1x1ODg2OCIsInVybCI6Ii9vcGVyYXRpb25hbC9saXN0L3NlcnZlci8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjozLCJtZW51X3RpdGxlIjoiXHU4ZmQwXHU3ZWY0XHU1ZGU1XHU1MTc3In0seyJpZCI6NywidGl0bGUiOiJcdTY3ZTVcdTc3MGJcdTY3MGRcdTUyYTFcdTU2NjgiLCJ1cmwiOiIvb3BlcmF0aW9uYWwvcmVhZC9zZXJ2ZXIvKFswLTldKykvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MywibWVudV90aXRsZSI6Ilx1OGZkMFx1N2VmNFx1NWRlNVx1NTE3NyJ9LHsiaWQiOjgsInRpdGxlIjoiXHU3ZjE2XHU4ZjkxXHU2NzBkXHU1MmExXHU1NjY4IiwidXJsIjoiL29wZXJhdGlvbmFsL2VkaXQvc2VydmVyLyhbMC05XSspLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjMsIm1lbnVfdGl0bGUiOiJcdThmZDBcdTdlZjRcdTVkZTVcdTUxNzcifSx7ImlkIjo5LCJ0aXRsZSI6Ilx1NTIyMFx1OTY2NFx1NjcwZFx1NTJhMVx1NTY2OCIsInVybCI6Ii9vcGVyYXRpb25hbC9kZWxldGUvc2VydmVyLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjMsIm1lbnVfdGl0bGUiOiJcdThmZDBcdTdlZjRcdTVkZTVcdTUxNzcifSx7ImlkIjoxMCwidGl0bGUiOiJcdTY3MGRcdTUyYTFcdTU2NjhcdTdlYzRcdTUyMTdcdTg4NjgiLCJ1cmwiOiIvb3BlcmF0aW9uYWwvbGlzdC9ncm91cC8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjozLCJtZW51X3RpdGxlIjoiXHU4ZmQwXHU3ZWY0XHU1ZGU1XHU1MTc3In0seyJpZCI6MTEsInRpdGxlIjoiXHU2ZGZiXHU1MmEwXHU2NzBkXHU1MmExXHU1NjY4IiwidXJsIjoiL29wZXJhdGlvbmFsL2NyZWF0ZS9zZXJ2ZXIvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MywibWVudV90aXRsZSI6Ilx1OGZkMFx1N2VmNFx1NWRlNVx1NTE3NyJ9LHsiaWQiOjEyLCJ0aXRsZSI6Ilx1NmRmYlx1NTJhMFx1NjcwZFx1NTJhMVx1NTY2OFx1N2VjNCIsInVybCI6Ii9vcGVyYXRpb25hbC9jcmVhdGUvZ3JvdXAvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MywibWVudV90aXRsZSI6Ilx1OGZkMFx1N2VmNFx1NWRlNVx1NTE3NyJ9LHsiaWQiOjEzLCJ0aXRsZSI6Ilx1NTIyMFx1OTY2NFx1NjcwZFx1NTJhMVx1NTY2OFx1N2VjNCIsInVybCI6Ii9vcGVyYXRpb25hbC9kZWxldGUvZ3JvdXAvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MywibWVudV90aXRsZSI6Ilx1OGZkMFx1N2VmNFx1NWRlNVx1NTE3NyJ9LHsiaWQiOjE0LCJ0aXRsZSI6Ilx1NGZlZVx1NjUzOVx1NjcwZFx1NTJhMVx1NTY2OFx1N2VjNCIsInVybCI6Ii9vcGVyYXRpb25hbC9lZGl0L2dyb3VwLyhbMC05XSspLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjMsIm1lbnVfdGl0bGUiOiJcdThmZDBcdTdlZjRcdTVkZTVcdTUxNzcifSx7ImlkIjoxNSwidGl0bGUiOiJcdTY3ZTVcdTc3MGJcdTY3MGRcdTUyYTFcdTU2NjhcdTdlYzQiLCJ1cmwiOiIvb3BlcmF0aW9uYWwvcmVhZC9ncm91cC8oWzAtOV0rKS8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjozLCJtZW51X3RpdGxlIjoiXHU4ZmQwXHU3ZWY0XHU1ZGU1XHU1MTc3In0seyJpZCI6MTYsInRpdGxlIjoiXHU5NjhmXHU2NzNhXHU1YmM2XHU3ODAxIiwidXJsIjoiL29wZXJhdGlvbmFsL2NyZWF0ZS9wYXNzd29yZC8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjozLCJtZW51X3RpdGxlIjoiXHU4ZmQwXHU3ZWY0XHU1ZGU1XHU1MTc3In0seyJpZCI6MTcsInRpdGxlIjoic3NoXHU4ZDI2XHU1M2Y3XHU1MjE3XHU4ODY4IiwidXJsIjoiL29wZXJhdGlvbmFsL3NlcnZlci9saXN0L3VzZXIvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MywibWVudV90aXRsZSI6Ilx1OGZkMFx1N2VmNFx1NWRlNVx1NTE3NyJ9LHsiaWQiOjE4LCJ0aXRsZSI6Ilx1NmRmYlx1NTJhMHNzaFx1OGQyNlx1NTNmNyIsInVybCI6Ii9vcGVyYXRpb25hbC9zZXJ2ZXIvY3JlYXRlL3VzZXIvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MywibWVudV90aXRsZSI6Ilx1OGZkMFx1N2VmNFx1NWRlNVx1NTE3NyJ9LHsiaWQiOjE5LCJ0aXRsZSI6Ilx1NTIyMFx1OTY2NHNzaFx1OGQyNlx1NTNmNyIsInVybCI6Ii9vcGVyYXRpb25hbC9zZXJ2ZXIvZGVsZXRlL3VzZXIvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MywibWVudV90aXRsZSI6Ilx1OGZkMFx1N2VmNFx1NWRlNVx1NTE3NyJ9LHsiaWQiOjIwLCJ0aXRsZSI6Ilx1NGZlZVx1NjUzOXNzaFx1OGQyNlx1NTNmNyIsInVybCI6Ii9vcGVyYXRpb25hbC9zZXJ2ZXIvZWRpdC91c2VyLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjMsIm1lbnVfdGl0bGUiOiJcdThmZDBcdTdlZjRcdTVkZTVcdTUxNzcifSx7ImlkIjoyMSwidGl0bGUiOiJcdTY3ZTVcdTc3MGJzc2hcdThkMjZcdTUzZjciLCJ1cmwiOiIvb3BlcmF0aW9uYWwvc2VydmVyL3JlYWQvdXNlci8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjozLCJtZW51X3RpdGxlIjoiXHU4ZmQwXHU3ZWY0XHU1ZGU1XHU1MTc3In0seyJpZCI6MjIsInRpdGxlIjoiXHU2NzQzXHU5NjUwXHU3YmExXHU3NDA2XHU1MjE3XHU4ODY4IiwidXJsIjoiL3Blcm1pc3Npb25zL2xpc3QvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6NiwibWVudV90aXRsZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiJ9LHsiaWQiOjIzLCJ0aXRsZSI6Ilx1NmRmYlx1NTJhMFx1OGQyNlx1NTNmNyIsInVybCI6Ii9wZXJtaXNzaW9ucy9jcmVhdGUvdXNlci8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjo2LCJtZW51X3RpdGxlIjoiXHU2NzQzXHU5NjUwXHU3YmExXHU3NDA2In0seyJpZCI6MjQsInRpdGxlIjoiXHU1MjIwXHU5NjY0XHU4ZDI2XHU1M2Y3IiwidXJsIjoiL3Blcm1pc3Npb25zL2RlbGV0ZS91c2VyLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjYsIm1lbnVfdGl0bGUiOiJcdTY3NDNcdTk2NTBcdTdiYTFcdTc0MDYifSx7ImlkIjoyNSwidGl0bGUiOiJcdTRmZWVcdTY1MzlcdThkMjZcdTUzZjciLCJ1cmwiOiIvcGVybWlzc2lvbnMvZWRpdC91c2VyLyhbMC05XSspLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjYsIm1lbnVfdGl0bGUiOiJcdTY3NDNcdTk2NTBcdTdiYTFcdTc0MDYifSx7ImlkIjoyNiwidGl0bGUiOiJcdThkMjZcdTUzZjdcdTUyMTdcdTg4NjgiLCJ1cmwiOiIvcGVybWlzc2lvbnMvbGlzdC91c2VyLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjYsIm1lbnVfdGl0bGUiOiJcdTY3NDNcdTk2NTBcdTdiYTFcdTc0MDYifSx7ImlkIjoyNywidGl0bGUiOiJcdTU0MmZcdTc1MjhcdTRlMGVcdTc5ODFcdTc1MjhcdThkMjZcdTUzZjciLCJ1cmwiOiIvcGVybWlzc2lvbnMvZGlzYWJsZS91c2VyLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjYsIm1lbnVfdGl0bGUiOiJcdTY3NDNcdTk2NTBcdTdiYTFcdTc0MDYifSx7ImlkIjoyOCwidGl0bGUiOiJcdTY2ZjRcdTY1MzlcdTY3NDNcdTk2NTAiLCJ1cmwiOiIvcGVybWlzc2lvbnMvY2hhbmdlL3Blcm1pc3Npb25zLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjYsIm1lbnVfdGl0bGUiOiJcdTY3NDNcdTk2NTBcdTdiYTFcdTc0MDYifSx7ImlkIjoyOSwidGl0bGUiOiJcdTY3NDNcdTk2NTBcdTRmZWVcdTY1MzlcdTUyMTdcdTg4NjgiLCJ1cmwiOiIvcGVybWlzc2lvbnMvZWRpdC8oWzAtOV0rKS8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjo2LCJtZW51X3RpdGxlIjoiXHU2NzQzXHU5NjUwXHU3YmExXHU3NDA2In0seyJpZCI6MzEsInRpdGxlIjoiXHU2ZGZiXHU1MmEwXHU4OWQyXHU4MjcyXHU3ZWM0IiwidXJsIjoiL3Blcm1pc3Npb25zL2NyZWF0ZS9yb2xlcy8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjo2LCJtZW51X3RpdGxlIjoiXHU2NzQzXHU5NjUwXHU3YmExXHU3NDA2In0seyJpZCI6MzIsInRpdGxlIjoiXHU1MjIwXHU5NjY0XHU4OWQyXHU4MjcyXHU3ZWM0IiwidXJsIjoiL3Blcm1pc3Npb25zL2RlbGV0ZS9yb2xlcy8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjo2LCJtZW51X3RpdGxlIjoiXHU2NzQzXHU5NjUwXHU3YmExXHU3NDA2In0seyJpZCI6MzMsInRpdGxlIjoiXHU2ZDQxXHU3YTBiXHU1MjE3XHU4ODY4IiwidXJsIjoiL3Byb2Nlc3MvbGlzdC8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjoyLCJtZW51X3RpdGxlIjoiXHU2ZDQxXHU3YTBiXHU3YmExXHU3NDA2In0seyJpZCI6MzQsInRpdGxlIjoiXHU2ZGZiXHU1MmEwXHU2ZDQxXHU3YTBiXHU4ODY4IiwidXJsIjoiL3Byb2Nlc3MvYWRkLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjIsIm1lbnVfdGl0bGUiOiJcdTZkNDFcdTdhMGJcdTdiYTFcdTc0MDYifSx7ImlkIjozNSwidGl0bGUiOiJcdTUyMjBcdTk2NjRcdTZkNDFcdTdhMGJcdTg4NjgiLCJ1cmwiOiIvcHJvY2Vzcy9kZWxldGUvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MiwibWVudV90aXRsZSI6Ilx1NmQ0MVx1N2EwYlx1N2JhMVx1NzQwNiJ9LHsiaWQiOjM2LCJ0aXRsZSI6Ilx1N2YxNlx1OGY5MVx1NmQ0MVx1N2EwYlx1ODg2OCIsInVybCI6Ii9wcm9jZXNzL2VkaXQvKFswLTldKykvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MiwibWVudV90aXRsZSI6Ilx1NmQ0MVx1N2EwYlx1N2JhMVx1NzQwNiJ9LHsiaWQiOjM3LCJ0aXRsZSI6Ilx1NjZmNFx1NjUzOVx1NmQ0MVx1N2EwYlx1ODg2OCIsInVybCI6Ii9wcm9jZXNzL3NhdmUvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MiwibWVudV90aXRsZSI6Ilx1NmQ0MVx1N2EwYlx1N2JhMVx1NzQwNiJ9LHsiaWQiOjM4LCJ0aXRsZSI6Ilx1NjdlNVx1NzcwYlx1NmQ0MVx1N2EwYlx1ODg2OCIsInVybCI6Ii9wcm9jZXNzL2luZm8vKFswLTldKykvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MiwibWVudV90aXRsZSI6Ilx1NmQ0MVx1N2EwYlx1N2JhMVx1NzQwNiJ9LHsiaWQiOjM5LCJ0aXRsZSI6Ilx1NTIxYlx1NWVmYVx1NmQ0MVx1N2EwYiIsInVybCI6Ii9wcm9jZXNzL2NyZWF0ZS8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjoyLCJtZW51X3RpdGxlIjoiXHU2ZDQxXHU3YTBiXHU3YmExXHU3NDA2In0seyJpZCI6NDAsInRpdGxlIjoiXHU2MjQwXHU2NzA5XHU2ZDQxXHU3YTBiXHU4YmIwXHU1ZjU1IiwidXJsIjoiL3Byb2Nlc3MvYWxsLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjIsIm1lbnVfdGl0bGUiOiJcdTZkNDFcdTdhMGJcdTdiYTFcdTc0MDYifSx7ImlkIjo0MSwidGl0bGUiOiJcdTZkNDFcdTdhMGJcdTViYTFcdTY4MzhcdTUyMTdcdTg4NjgiLCJ1cmwiOiIvcHJvY2Vzcy9hdWRpdC9saXN0LyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjIsIm1lbnVfdGl0bGUiOiJcdTZkNDFcdTdhMGJcdTdiYTFcdTc0MDYifSx7ImlkIjo0MiwidGl0bGUiOiJcdTViYTFcdTY4MzhcdTZkNDFcdTdhMGIiLCJ1cmwiOiIvcHJvY2Vzcy9hdWRpdC9hdXRoLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjIsIm1lbnVfdGl0bGUiOiJcdTZkNDFcdTdhMGJcdTdiYTFcdTc0MDYifSx7ImlkIjo0MywidGl0bGUiOiJcdTk4NzlcdTc2ZWVcdTdiYTFcdTc0MDZcdTUyMTdcdTg4NjgiLCJ1cmwiOiIvcHJvamVjdC9saXN0LyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjUsIm1lbnVfdGl0bGUiOiJcdTk4NzlcdTc2ZWVcdTdiYTFcdTc0MDYifSx7ImlkIjo0NCwidGl0bGUiOiJcdTZkZmJcdTUyYTBcdTk4NzlcdTc2ZWUiLCJ1cmwiOiIvcHJvamVjdC9jcmVhdGUvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6NSwibWVudV90aXRsZSI6Ilx1OTg3OVx1NzZlZVx1N2JhMVx1NzQwNiJ9LHsiaWQiOjQ1LCJ0aXRsZSI6Ilx1NTIyMFx1OTY2NFx1OTg3OVx1NzZlZSIsInVybCI6Ii9wcm9qZWN0L2RlbGV0ZS8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjo1LCJtZW51X3RpdGxlIjoiXHU5ODc5XHU3NmVlXHU3YmExXHU3NDA2In0seyJpZCI6NDYsInRpdGxlIjoiXHU0ZmVlXHU2NTM5XHU5ODc5XHU3NmVlIiwidXJsIjoiL3Byb2plY3QvZWRpdC8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjo1LCJtZW51X3RpdGxlIjoiXHU5ODc5XHU3NmVlXHU3YmExXHU3NDA2In0seyJpZCI6NDcsInRpdGxlIjoiXHU2N2U1XHU3NzBiXHU5ODc5XHU3NmVlIiwidXJsIjoiL3Byb2plY3QvcmVhZC8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjo1LCJtZW51X3RpdGxlIjoiXHU5ODc5XHU3NmVlXHU3YmExXHU3NDA2In0seyJpZCI6NDgsInRpdGxlIjoiXHU4ZmRlXHU2M2E1XHU2ZDRiXHU4YmQ1IiwidXJsIjoiL3Byb2plY3QvY29ubmVjdGlvbi90ZXN0LyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjUsIm1lbnVfdGl0bGUiOiJcdTk4NzlcdTc2ZWVcdTdiYTFcdTc0MDYifSx7ImlkIjo0OSwidGl0bGUiOiJcdTUzZDFcdTVlMDNcdTY2ZjRcdTY1YjBcdTk4NzlcdTc2ZWUiLCJ1cmwiOiIvcHJvamVjdC9yZWxlYXNlLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjUsIm1lbnVfdGl0bGUiOiJcdTk4NzlcdTc2ZWVcdTdiYTFcdTc0MDYifSx7ImlkIjo1MCwidGl0bGUiOiJcdTgzYjdcdTUzZDZ0YWdcdTY4MDdcdTdiN2UiLCJ1cmwiOiIvcHJvamVjdC90YWcvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6NSwibWVudV90aXRsZSI6Ilx1OTg3OVx1NzZlZVx1N2JhMVx1NzQwNiJ9LHsiaWQiOjUxLCJ0aXRsZSI6Ilx1NTZkZVx1NmVkYVx1OTg3OVx1NzZlZSIsInVybCI6Ii9wcm9qZWN0L3JvbGxiYWNrLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjUsIm1lbnVfdGl0bGUiOiJcdTk4NzlcdTc2ZWVcdTdiYTFcdTc0MDYifV0sInVzZXIiOiJhZG1pbiIsInRvdGFsX251bSI6NSwiYXZhdGFyIjoic3RhdGljL2F2YXRhci8xNTcxMjkyNjkxMjE3NjY2NF9hdmF0YXIuanBnIn0=','2019-10-31 07:15:39.123183'),('n2c7tzdk22hzheaqfhp2cj5shxa2xagg','OWFiMTk4YzY2ZjI1Y2VhZTU5M2YyZTlhMGNmZjhiOTI3ZmRlYWRjYjp7InBlcm1pc3Npb25fdXJsX2xpc3QiOnsiNCI6eyJjb2RlIjpbIjMiLCIzIl0sInVybHMiOlsiL29wZXJhdGlvbmFsL2VkaXQvc2VydmVyLyhbMC05XSspLyIsIi9vcGVyYXRpb25hbC9zZXJ2ZXIvY3JlYXRlL3VzZXIvIl19LCIzIjp7ImNvZGUiOlsiNiIsIjYiXSwidXJscyI6WyIvcGVybWlzc2lvbnMvZGVsZXRlL3VzZXIvIiwiL3Blcm1pc3Npb25zL2NoYW5nZS9wZXJtaXNzaW9ucy8iXX0sIjIiOnsiY29kZSI6WyIyIiwiMiJdLCJ1cmxzIjpbIi9wcm9jZXNzL2luZm8vKFswLTldKykvIiwiL3Byb2Nlc3MvY3JlYXRlLyJdfSwiMSI6eyJjb2RlIjpbIjUiLCI1IiwiNSJdLCJ1cmxzIjpbIi9wcm9qZWN0L2xpc3QvIiwiL3Byb2plY3QvY3JlYXRlLyIsIi9wcm9qZWN0L2Nvbm5lY3Rpb24vdGVzdC8iXX19LCJwZXJtaXNzaW9uX21lbnVfbGlzdCI6W3siaWQiOjgsInRpdGxlIjoiXHU3ZjE2XHU4ZjkxXHU2NzBkXHU1MmExXHU1NjY4IiwidXJsIjoiL29wZXJhdGlvbmFsL2VkaXQvc2VydmVyLyhbMC05XSspLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjMsIm1lbnVfdGl0bGUiOiJcdThmZDBcdTdlZjRcdTVkZTVcdTUxNzcifSx7ImlkIjoxOCwidGl0bGUiOiJcdTZkZmJcdTUyYTBzc2hcdThkMjZcdTUzZjciLCJ1cmwiOiIvb3BlcmF0aW9uYWwvc2VydmVyL2NyZWF0ZS91c2VyLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjMsIm1lbnVfdGl0bGUiOiJcdThmZDBcdTdlZjRcdTVkZTVcdTUxNzcifSx7ImlkIjoyNCwidGl0bGUiOiJcdTUyMjBcdTk2NjRcdThkMjZcdTUzZjciLCJ1cmwiOiIvcGVybWlzc2lvbnMvZGVsZXRlL3VzZXIvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6NiwibWVudV90aXRsZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiJ9LHsiaWQiOjI4LCJ0aXRsZSI6Ilx1NjZmNFx1NjUzOVx1Njc0M1x1OTY1MCIsInVybCI6Ii9wZXJtaXNzaW9ucy9jaGFuZ2UvcGVybWlzc2lvbnMvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6NiwibWVudV90aXRsZSI6Ilx1Njc0M1x1OTY1MFx1N2JhMVx1NzQwNiJ9LHsiaWQiOjM4LCJ0aXRsZSI6Ilx1NjdlNVx1NzcwYlx1NmQ0MVx1N2EwYlx1ODg2OCIsInVybCI6Ii9wcm9jZXNzL2luZm8vKFswLTldKykvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6MiwibWVudV90aXRsZSI6Ilx1NmQ0MVx1N2EwYlx1N2JhMVx1NzQwNiJ9LHsiaWQiOjM5LCJ0aXRsZSI6Ilx1NTIxYlx1NWVmYVx1NmQ0MVx1N2EwYiIsInVybCI6Ii9wcm9jZXNzL2NyZWF0ZS8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjoyLCJtZW51X3RpdGxlIjoiXHU2ZDQxXHU3YTBiXHU3YmExXHU3NDA2In0seyJpZCI6NDMsInRpdGxlIjoiXHU5ODc5XHU3NmVlXHU3YmExXHU3NDA2XHU1MjE3XHU4ODY4IiwidXJsIjoiL3Byb2plY3QvbGlzdC8iLCJtZW51X2dwX2lkIjpudWxsLCJtZW51X2lkIjo1LCJtZW51X3RpdGxlIjoiXHU5ODc5XHU3NmVlXHU3YmExXHU3NDA2In0seyJpZCI6NDQsInRpdGxlIjoiXHU2ZGZiXHU1MmEwXHU5ODc5XHU3NmVlIiwidXJsIjoiL3Byb2plY3QvY3JlYXRlLyIsIm1lbnVfZ3BfaWQiOm51bGwsIm1lbnVfaWQiOjUsIm1lbnVfdGl0bGUiOiJcdTk4NzlcdTc2ZWVcdTdiYTFcdTc0MDYifSx7ImlkIjo0OCwidGl0bGUiOiJcdThmZGVcdTYzYTVcdTZkNGJcdThiZDUiLCJ1cmwiOiIvcHJvamVjdC9jb25uZWN0aW9uL3Rlc3QvIiwibWVudV9ncF9pZCI6bnVsbCwibWVudV9pZCI6NSwibWVudV90aXRsZSI6Ilx1OTg3OVx1NzZlZVx1N2JhMVx1NzQwNiJ9XSwidXNlciI6InRlc3QiLCJ0b3RhbF9udW0iOjUsImF2YXRhciI6InN0YXRpYy9hdmF0YXIvZGVmYXVsdF9hdmF0YXIuanBnIiwiaXNfbG9naW4iOnRydWV9','2019-10-31 06:27:47.369671');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operational_group`
--

DROP TABLE IF EXISTS `operational_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operational_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operational_group`
--

LOCK TABLES `operational_group` WRITE;
/*!40000 ALTER TABLE `operational_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `operational_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operational_server`
--

DROP TABLE IF EXISTS `operational_server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operational_server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_name` varchar(32) NOT NULL,
  `ip` varchar(15) NOT NULL,
  `user` varchar(12) DEFAULT NULL,
  `password` varchar(32) DEFAULT NULL,
  `port` int(11) DEFAULT NULL,
  `status` varchar(4) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `server_name` (`server_name`),
  UNIQUE KEY `ip` (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operational_server`
--

LOCK TABLES `operational_server` WRITE;
/*!40000 ALTER TABLE `operational_server` DISABLE KEYS */;
/*!40000 ALTER TABLE `operational_server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operational_server_groups`
--

DROP TABLE IF EXISTS `operational_server_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operational_server_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `server_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `operational_server_groups_server_id_group_id_f3ba3222_uniq` (`server_id`,`group_id`),
  KEY `operational_server_g_group_id_c9a0b20b_fk_operation` (`group_id`),
  CONSTRAINT `operational_server_g_group_id_c9a0b20b_fk_operation` FOREIGN KEY (`group_id`) REFERENCES `operational_group` (`id`),
  CONSTRAINT `operational_server_g_server_id_04f19792_fk_operation` FOREIGN KEY (`server_id`) REFERENCES `operational_server` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operational_server_groups`
--

LOCK TABLES `operational_server_groups` WRITE;
/*!40000 ALTER TABLE `operational_server_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `operational_server_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operational_serveruser`
--

DROP TABLE IF EXISTS `operational_serveruser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operational_serveruser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(32) NOT NULL,
  `senior` int(11) NOT NULL,
  `uid` int(11) DEFAULT NULL,
  `gid` int(11) DEFAULT NULL,
  `sudo` varchar(1024) DEFAULT NULL,
  `create_time` varchar(32) DEFAULT NULL,
  `way` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operational_serveruser`
--

LOCK TABLES `operational_serveruser` WRITE;
/*!40000 ALTER TABLE `operational_serveruser` DISABLE KEYS */;
/*!40000 ALTER TABLE `operational_serveruser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operational_serveruser_groups`
--

DROP TABLE IF EXISTS `operational_serveruser_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operational_serveruser_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serveruser_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `operational_serveruser_g_serveruser_id_group_id_21bec149_uniq` (`serveruser_id`,`group_id`),
  KEY `operational_serverus_group_id_3db9da65_fk_operation` (`group_id`),
  CONSTRAINT `operational_serverus_group_id_3db9da65_fk_operation` FOREIGN KEY (`group_id`) REFERENCES `operational_group` (`id`),
  CONSTRAINT `operational_serverus_serveruser_id_5c0e2175_fk_operation` FOREIGN KEY (`serveruser_id`) REFERENCES `operational_serveruser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operational_serveruser_groups`
--

LOCK TABLES `operational_serveruser_groups` WRITE;
/*!40000 ALTER TABLE `operational_serveruser_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `operational_serveruser_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operational_serveruser_servers`
--

DROP TABLE IF EXISTS `operational_serveruser_servers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `operational_serveruser_servers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `serveruser_id` int(11) NOT NULL,
  `server_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `operational_serveruser_s_serveruser_id_server_id_e39970f8_uniq` (`serveruser_id`,`server_id`),
  KEY `operational_serverus_server_id_23061c2a_fk_operation` (`server_id`),
  CONSTRAINT `operational_serverus_server_id_23061c2a_fk_operation` FOREIGN KEY (`server_id`) REFERENCES `operational_server` (`id`),
  CONSTRAINT `operational_serverus_serveruser_id_492b3159_fk_operation` FOREIGN KEY (`serveruser_id`) REFERENCES `operational_serveruser` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operational_serveruser_servers`
--

LOCK TABLES `operational_serveruser_servers` WRITE;
/*!40000 ALTER TABLE `operational_serveruser_servers` DISABLE KEYS */;
/*!40000 ALTER TABLE `operational_serveruser_servers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions_group`
--

DROP TABLE IF EXISTS `permissions_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `menu_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `permissions_group_menu_id_2ab1f2b1_fk_permissions_menu_id` (`menu_id`),
  CONSTRAINT `permissions_group_menu_id_2ab1f2b1_fk_permissions_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `permissions_menu` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions_group`
--

LOCK TABLES `permissions_group` WRITE;
/*!40000 ALTER TABLE `permissions_group` DISABLE KEYS */;
INSERT INTO `permissions_group` VALUES (1,'project',5),(2,'process',2),(3,'permissions',6),(4,'operational',3),(5,'configuration',4),(6,'website',1);
/*!40000 ALTER TABLE `permissions_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions_menu`
--

DROP TABLE IF EXISTS `permissions_menu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions_menu`
--

LOCK TABLES `permissions_menu` WRITE;
/*!40000 ALTER TABLE `permissions_menu` DISABLE KEYS */;
INSERT INTO `permissions_menu` VALUES (1,'网站导航'),(2,'流程管理'),(3,'运维工具'),(4,'系统设置'),(5,'项目管理'),(6,'权限管理');
/*!40000 ALTER TABLE `permissions_menu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions_permission`
--

DROP TABLE IF EXISTS `permissions_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `url` varchar(64) NOT NULL,
  `codes` varchar(32) NOT NULL,
  `group_id` int(11) NOT NULL,
  `menu_gp_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `permissions_permission_group_id_8f809304_fk_permissions_group_id` (`group_id`),
  KEY `permissions_permissi_menu_gp_id_bf15b90a_fk_permissio` (`menu_gp_id`),
  CONSTRAINT `permissions_permissi_menu_gp_id_bf15b90a_fk_permissio` FOREIGN KEY (`menu_gp_id`) REFERENCES `permissions_permission` (`id`),
  CONSTRAINT `permissions_permission_group_id_8f809304_fk_permissions_group_id` FOREIGN KEY (`group_id`) REFERENCES `permissions_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions_permission`
--

LOCK TABLES `permissions_permission` WRITE;
/*!40000 ALTER TABLE `permissions_permission` DISABLE KEYS */;
INSERT INTO `permissions_permission` VALUES (1,'添加导航','/add/navigation/','1',6,NULL),(2,'删除导航','/delete/navigation/','1',6,NULL),(3,'修改邮箱','/configuration/edit/email/','4',5,NULL),(4,'修改密码','/configuration/edit/password/','4',5,NULL),(5,'修改头像','/configuration/edit/avatar/','4',5,NULL),(6,'服务器管理列表','/operational/list/server/','3',4,NULL),(7,'查看服务器','/operational/read/server/([0-9]+)/','3',4,NULL),(8,'编辑服务器','/operational/edit/server/([0-9]+)/','3',4,NULL),(9,'删除服务器','/operational/delete/server/','3',4,NULL),(10,'服务器组列表','/operational/list/group/','3',4,NULL),(11,'添加服务器','/operational/create/server/','3',4,NULL),(12,'添加服务器组','/operational/create/group/','3',4,NULL),(13,'删除服务器组','/operational/delete/group/','3',4,NULL),(14,'修改服务器组','/operational/edit/group/([0-9]+)/','3',4,NULL),(15,'查看服务器组','/operational/read/group/([0-9]+)/','3',4,NULL),(16,'随机密码','/operational/create/password/','3',4,NULL),(17,'ssh账号列表','/operational/server/list/user/','3',4,NULL),(18,'添加ssh账号','/operational/server/create/user/','3',4,NULL),(19,'删除ssh账号','/operational/server/delete/user/','3',4,NULL),(20,'修改ssh账号','/operational/server/edit/user/','3',4,NULL),(21,'查看ssh账号','/operational/server/read/user/','3',4,NULL),(22,'权限管理列表','/permissions/list/','6',3,NULL),(23,'添加账号','/permissions/create/user/','6',3,NULL),(24,'删除账号','/permissions/delete/user/','6',3,NULL),(25,'修改账号','/permissions/edit/user/([0-9]+)/','6',3,NULL),(26,'账号列表','/permissions/list/user/','6',3,NULL),(27,'启用与禁用账号','/permissions/disable/user/','6',3,NULL),(28,'更改权限','/permissions/change/permissions/','6',3,NULL),(29,'权限修改列表','/permissions/edit/([0-9]+)/','6',3,NULL),(31,'添加角色组','/permissions/create/roles/','6',3,NULL),(32,'删除角色组','/permissions/delete/roles/','6',3,NULL),(33,'流程列表','/process/list/','2',2,NULL),(34,'添加流程表','/process/add/','2',2,NULL),(35,'删除流程表','/process/delete/','2',2,NULL),(36,'编辑流程表','/process/edit/([0-9]+)/','2',2,NULL),(37,'更改流程表','/process/save/','2',2,NULL),(38,'查看流程表','/process/info/([0-9]+)/','2',2,NULL),(39,'创建流程','/process/create/','2',2,NULL),(40,'所有流程记录','/process/all/','2',2,NULL),(41,'流程审核列表','/process/audit/list/','2',2,NULL),(42,'审核流程','/process/audit/auth/','2',2,NULL),(43,'项目管理列表','/project/list/','5',1,NULL),(44,'添加项目','/project/create/','5',1,NULL),(45,'删除项目','/project/delete/','5',1,NULL),(46,'修改项目','/project/edit/','5',1,NULL),(47,'查看项目','/project/read/','5',1,NULL),(48,'连接测试','/project/connection/test/','5',1,NULL),(49,'发布更新项目','/project/release/','5',1,NULL),(50,'获取tag标签','/project/tag/','5',1,NULL),(51,'回滚项目','/project/rollback/','5',1,NULL);
/*!40000 ALTER TABLE `permissions_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions_role`
--

DROP TABLE IF EXISTS `permissions_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions_role`
--

LOCK TABLES `permissions_role` WRITE;
/*!40000 ALTER TABLE `permissions_role` DISABLE KEYS */;
INSERT INTO `permissions_role` VALUES (1,'管理员'),(2,'游客');
/*!40000 ALTER TABLE `permissions_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions_role_permissions`
--

DROP TABLE IF EXISTS `permissions_role_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions_role_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `permissions_role_permissions_role_id_permission_id_ea4429c8_uniq` (`role_id`,`permission_id`),
  KEY `permissions_role_per_permission_id_cd4f2c07_fk_permissio` (`permission_id`),
  CONSTRAINT `permissions_role_per_permission_id_cd4f2c07_fk_permissio` FOREIGN KEY (`permission_id`) REFERENCES `permissions_permission` (`id`),
  CONSTRAINT `permissions_role_per_role_id_9313389c_fk_permissio` FOREIGN KEY (`role_id`) REFERENCES `permissions_role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions_role_permissions`
--

LOCK TABLES `permissions_role_permissions` WRITE;
/*!40000 ALTER TABLE `permissions_role_permissions` DISABLE KEYS */;
INSERT INTO `permissions_role_permissions` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,1,6),(7,1,7),(8,1,8),(9,1,9),(10,1,10),(11,1,11),(12,1,12),(13,1,13),(14,1,14),(15,1,15),(16,1,16),(17,1,17),(18,1,18),(19,1,19),(20,1,20),(21,1,21),(22,1,22),(23,1,23),(24,1,24),(25,1,25),(26,1,26),(27,1,27),(28,1,28),(29,1,29),(30,1,31),(31,1,32),(32,1,33),(33,1,34),(34,1,35),(35,1,36),(36,1,37),(37,1,38),(38,1,39),(39,1,40),(40,1,41),(41,1,42),(42,1,43),(43,1,44),(44,1,45),(45,1,46),(46,1,47),(47,1,48),(48,1,49),(49,1,50),(50,1,51),(70,2,8),(73,2,18),(71,2,24),(74,2,47),(72,2,48);
/*!40000 ALTER TABLE `permissions_role_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions_user`
--

DROP TABLE IF EXISTS `permissions_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  `email` varchar(32) NOT NULL,
  `head_img` varchar(512) NOT NULL,
  `create_time` varchar(64) NOT NULL,
  `disable` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions_user`
--

LOCK TABLES `permissions_user` WRITE;
/*!40000 ALTER TABLE `permissions_user` DISABLE KEYS */;
INSERT INTO `permissions_user` VALUES (1,'admin','admin','123456','admin@qq.com','static/avatar/15712926912176664_avatar.jpg','2019-10-17 10:27:12',0);
/*!40000 ALTER TABLE `permissions_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions_user_roles`
--

DROP TABLE IF EXISTS `permissions_user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permissions_user_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `permissions_user_roles_user_id_role_id_5aecc20d_uniq` (`user_id`,`role_id`),
  KEY `permissions_user_roles_role_id_64e0ace6_fk_permissions_role_id` (`role_id`),
  CONSTRAINT `permissions_user_roles_role_id_64e0ace6_fk_permissions_role_id` FOREIGN KEY (`role_id`) REFERENCES `permissions_role` (`id`),
  CONSTRAINT `permissions_user_roles_user_id_6941002b_fk_permissions_user_id` FOREIGN KEY (`user_id`) REFERENCES `permissions_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions_user_roles`
--

LOCK TABLES `permissions_user_roles` WRITE;
/*!40000 ALTER TABLE `permissions_user_roles` DISABLE KEYS */;
INSERT INTO `permissions_user_roles` VALUES (4,1,1);
/*!40000 ALTER TABLE `permissions_user_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_intermediate`
--

DROP TABLE IF EXISTS `process_intermediate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_intermediate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `describe` varchar(512) DEFAULT NULL,
  `attachment` varchar(512) DEFAULT NULL,
  `process_str` varchar(256) NOT NULL,
  `user` varchar(8) NOT NULL,
  `create_time` varchar(128) DEFAULT NULL,
  `status` varchar(8) NOT NULL,
  `is_read` int(11) NOT NULL,
  `create_user_id` int(11) NOT NULL,
  `process_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `process_intermediate_create_user_id_6eb4752c_fk_permissio` (`create_user_id`),
  KEY `process_intermediate_process_id_bac9cba3_fk_process_process_id` (`process_id`),
  CONSTRAINT `process_intermediate_create_user_id_6eb4752c_fk_permissio` FOREIGN KEY (`create_user_id`) REFERENCES `permissions_user` (`id`),
  CONSTRAINT `process_intermediate_process_id_bac9cba3_fk_process_process_id` FOREIGN KEY (`process_id`) REFERENCES `process_process` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_intermediate`
--

LOCK TABLES `process_intermediate` WRITE;
/*!40000 ALTER TABLE `process_intermediate` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_intermediate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_process`
--

DROP TABLE IF EXISTS `process_process`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_process` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `process` varchar(256) NOT NULL,
  `describe` varchar(512) NOT NULL,
  `create_time` varchar(128) NOT NULL,
  `change_time` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_process`
--

LOCK TABLES `process_process` WRITE;
/*!40000 ALTER TABLE `process_process` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_process` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_log`
--

DROP TABLE IF EXISTS `project_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `git_tag` varchar(64) NOT NULL,
  `git_commit` varchar(256) NOT NULL,
  `text` varchar(10240) NOT NULL,
  `new_time` varchar(18) NOT NULL,
  `operation_user` varchar(18) NOT NULL,
  `on_version_log_id` int(11) DEFAULT NULL,
  `count_num` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_log`
--

LOCK TABLES `project_log` WRITE;
/*!40000 ALTER TABLE `project_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_project`
--

DROP TABLE IF EXISTS `project_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_project` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(64) NOT NULL,
  `create_time` varchar(32) DEFAULT NULL,
  `change_time` varchar(32) DEFAULT NULL,
  `describe` varchar(512) DEFAULT NULL,
  `git_url` varchar(128) DEFAULT NULL,
  `git_auth_way` int(11) NOT NULL,
  `git_user` varchar(16) DEFAULT NULL,
  `git_password` varchar(64) DEFAULT NULL,
  `git_branch` varchar(16) NOT NULL,
  `deploy_dir` varchar(512) NOT NULL,
  `exclude_file` varchar(4096) DEFAULT NULL,
  `online_notice` varchar(16) NOT NULL,
  `dingding_notice` varchar(128) DEFAULT NULL,
  `work_dir` varchar(128) DEFAULT NULL,
  `connection_auth` int(11) NOT NULL,
  `create_user_id` int(11) NOT NULL,
  `email_notice_id` int(11) DEFAULT NULL,
  `log_id` int(11) DEFAULT NULL,
  `server_group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `project_project_create_user_id_164687df_fk_permissions_user_id` (`create_user_id`),
  KEY `project_project_email_notice_id_ca35ee56_fk_permissions_role_id` (`email_notice_id`),
  KEY `project_project_log_id_925e2a55_fk_project_log_id` (`log_id`),
  KEY `project_project_server_group_id_daa38e13_fk_operational_group_id` (`server_group_id`),
  CONSTRAINT `project_project_create_user_id_164687df_fk_permissions_user_id` FOREIGN KEY (`create_user_id`) REFERENCES `permissions_user` (`id`),
  CONSTRAINT `project_project_email_notice_id_ca35ee56_fk_permissions_role_id` FOREIGN KEY (`email_notice_id`) REFERENCES `permissions_role` (`id`),
  CONSTRAINT `project_project_log_id_925e2a55_fk_project_log_id` FOREIGN KEY (`log_id`) REFERENCES `project_log` (`id`),
  CONSTRAINT `project_project_server_group_id_daa38e13_fk_operational_group_id` FOREIGN KEY (`server_group_id`) REFERENCES `operational_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_project`
--

LOCK TABLES `project_project` WRITE;
/*!40000 ALTER TABLE `project_project` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_project` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-17 15:27:09
