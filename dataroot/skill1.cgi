
sub SKILL1{
$ksub2=0;
open(IN,"$SKILL_LIST");
@SKILL_DATA = <IN>;
close(IN);
($dk,$eskillcode,$eskillpoint) = split(/<>/,$SKILL_DATA[$cnum]);
&SKILL;
if($eskillpoint > $kpoint){
&K_LOG("$mmonth�� : $name�� ���⿡�� ��ų����Ʈ�� ������� �ʽ��ϴ�. (�ʿ�SP : $eskillpoint)");
}else{
$kqpoint = 1 if $kcodea =~ /C9/;
$kpoint -= $eskillpoint;
$kskill .= $eskillcode;
&K_LOG("$mmonth�� : Ư�� $name�� ������ϴ�.");
&MAP_LOG("<img src=$IMG/j24.gif> $kname���� $name�� ������ϴ�.");
}
}
1;

