
sub BOKJANG{
						$ksub2=0;
						open(IN,"$PRO_LIST");
						@PRO_DATA = <IN>;
						close(IN);
						($proname,$proval,$prodmg,$prowei,$proele,$prosta,$proclass,$protownid) = split(/<>/,$PRO_DATA[$cnum]);
						($proname2,$proval2) = split(/<>/,$PRO_DATA[$kbook]);
						$proval2 = int($proval2 * 0.6);
						if($proval > $kgold + $proval2){
							&K_LOG("$mmonth�� : �������� ������� �ʽ��ϴ�. $proname (�� : $proval)");
						}else{
							$kgold += $proval2;
							$kgold -= $proval;
							$kbook = $cnum;
							&K_LOG("$mmonth�� : ���� : $proname�� �����߽��ϴ�.");
							&HISTORY_LOG($kid,"$proname�� �����߽��ϴ�.");
						}
}
1;

