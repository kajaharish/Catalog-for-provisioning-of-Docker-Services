#!/usr/bin/python2

import FetchCookie as fc
import ConnectDatabase as cd

print ("Content-Type: text/html \n\n")

class Dashboard:
    
    def __init__(self):
        self.username = None
        self.cookie = None
        self.database = cd.Database()

    def getCookieValue(self):
        self.cookie = fc.getCookieValue()

    def getUserName(self):
        check = self.database.cursor.execute('select username from session where session_id = "%s"'%(self.cookie))
        self.username = self.database.cursor.fetchone()[0]
    
    
    def generateContainer(self):
        check = self.database.cursor.execute('select container_name from container where username = "%s"'%(self.username))
        result = self.database.cursor.fetchall()
        string = ""

#Code is needed to be completed from here.
        for x in result:
            

        '''
        <div class="cont">
        <img src="images/container.png" alt="Avatar" class="image" >Container 1
        <div class="middle" value="container">
        <div class="text">File manager</div>
        </div>
        </div>
        '''


if __name__ == "__main__":
    
    dashboard = Dashboard()
    dashboard.getCookieValue()
    dashboard.getUserName()
    dashboard.generateContainer()


'''
    print 
<!doctype html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
<!--[if gt IE 8]><!--> 
	
<html class="no-js" lang=""> <!--<![endif]-->
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Hostinger Admin - HTML5 Admin Template</title>
    <meta name="description" content="Sufee Admin - HTML5 Admin Template">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <link rel="apple-touch-icon" href="apple-icon.png">
    <link rel="shortcut icon" href="favicon.ico">

    <link rel="stylesheet" href="./css/normalize.css" type="text/css">
    <link rel="stylesheet" href="./css/bootstrap.min.css" type="text/css">
    <link rel="stylesheet" href="./css/font-awesome.min.css" type="text/css">
    <link rel="stylesheet" href="./css/themify-icons.css" type="text/css">
	<link rel="stylesheet" href="./scripts/css/style2.css" type="text/css">
    <link rel="stylesheet" href="./css/flag-icon.min.css" type="text/css">
    <link rel="stylesheet" href="./css/cs-skin-elastic.css" type="text/css">
    <!-- <link rel="stylesheet" href="assets/css/bootstrap-select.less"> -->
    <link rel="stylesheet" href="./css/style.css" type="text/css">
    

    <link href='https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800' rel='stylesheet' type='text/css'>

    <!-- <script type="text/javascript" src="https://cdn.jsdelivr.net/html5shiv/3.7.3/html5shiv.min.js"></script> -->

</head>
<body >


        <!-- Left Panel -->

    <aside id="left-panel" class="left-panel">
        <nav class="navbar navbar-expand-sm navbar-default">

            <div class="navbar-header">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#main-menu" aria-controls="main-menu" aria-expanded="false" aria-label="Toggle navigation">
                    <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand" href="dashboard.html"><img src="images/logo.png" alt="Logo"></a>
                <a class="navbar-brand hidden" href="dashboard.html"><img src="images/logo2.png" alt="Logo"></a>
            </div>

            <div id="main-menu" class="main-menu collapse navbar-collapse">
                <ul class="nav navbar-nav">
                    <li class="active">
                        <a href="dashboard.html"> <i class="menu-icon fa fa-dashboard"></i> Dashboard </a>
                    </li>
					
					<!-- <li> -->
                        <!-- <a href="index.html"> <i class="menu-icon fa fa-arrow-circle-o-up"></i>Update Container</a> -->
                    <!-- </li> -->
					
					<li>
                        <a href="delete.html"> <i class="menu-icon fa fa-trash-o"></i>Delete Container</a>
                    </li>
					
					<li>
                        <a href="add.html"> <i class="menu-icon fa fa-plus-square"></i>Add a Container</a>
                    </li>
					
					<li>
                        <a href="status.html"> <i class="menu-icon fa fa-bar-chart"></i>Status</a>
                    </li>
                    
                </ul>
            </div><!-- /.navbar-collapse -->
        </nav>
    </aside><!-- /#left-panel -->

    <!-- Left Panel -->
    <!-- Right Panel -->

    <div id="right-panel" class="right-panel">

        <!-- Header-->
        <header id="header" class="header">

            <div class="header-menu">

                <div class="col-sm-7">
                    <a id="menuToggle" class="menutoggle pull-left"><i class="fa fa fa-tasks"></i></a>
                    
                </div>

                <div class="col-sm-5">
                    <div class="user-area dropdown float-right">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            <img class="user-avatar rounded-circle" src="images/admin.jpg" alt="User Avatar">
                        </a>

                        <div class="user-menu dropdown-menu">
                                <a class="nav-link" href="profile.html"><i class="fa fa- user"></i>My Profile</a>

                                <a class="nav-link" href="#"><i class="fa fa- user"></i>Notifications <span class="count">13</span></a>

                                <a class="nav-link" href="#"><i class="fa fa -cog"></i>Settings</a>

                                <a class="nav-link" href="#"><i class="fa fa-power -off"></i>Logout</a>
                        </div>
                    </div>

                </div>
            </div>

        </header><!-- /header -->
        <!-- Header-->

        <div class="breadcrumbs">
            <div class="col-sm-4">
                <div class="page-header float-left">
                    <div class="page-title">
                        <h1>Dashboard</h1>
                    </div>
                </div>
            </div>
            <div class="col-sm-8">
                <div class="page-header float-right">
                    <div class="page-title">
                        <ol class="breadcrumb text-right">
                            <li class="active">Dashboard</li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>
	
	<!--main body end-->
'''

#This portion of code generates containers at the runtime.
'''
        <div class="cont">
			<img src="images/container.png" alt="Avatar" class="image" >Container 1
				<div class="middle" value="container">
					<div class="text">File manager</div>
				</div>
		</div>
'''

'''
		
    </div><!-- /#right-panel -->

    <!-- Right Panel -->

    <script src="./js/vendor/jquery-2.1.4.min.js" type="text/javascript"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" type="text/javascript"></script>
    <script src="./js/plugins.js" type="text/javascript"></script>
    <script src="./js/main.js" type="text/javascript"></script>


    <script src="./js/lib/chart-js/Chart.bundle.js" type="text/javascript"></script>
    <script src="./js/dashboard.js" type="text/javascript"></script>
    <script src="./js/widgets.js" type="text/javascript"></script>
    <script src="./js/lib/vector-map/jquery.vmap.js" type="text/javascript"></script>
    <script src="./js/lib/vector-map/jquery.vmap.min.js" type="text/javascript"></script>
    <script src="./js/lib/vector-map/jquery.vmap.sampledata.js" type="text/javascript"></script>
    <script src="./js/lib/vector-map/country/jquery.vmap.world.js" type="text/javascript"></script>
    <script>
        ( function ( $ ) {
            "use strict";

            jQuery( '#vmap' ).vectorMap( {
                map: 'world_en',
                backgroundColor: null,
                color: '#ffffff',
                hoverOpacity: 0.7,
                selectedColor: '#1de9b6',
                enableZoom: true,
                showTooltip: true,
                values: sample_data,
                scaleColors: [ '#1de9b6', '#03a9f5' ],
                normalizeFunction: 'polynomial'
            } );
        } )( jQuery );
    </script>

</body>
</html>
'''
