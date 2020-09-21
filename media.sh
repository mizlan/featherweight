afplay_pid() {
	ps aux | grep 'afplay' | grep -v 'grep' | awk '{print $2}'
}

pause_af() {
	kill -17 $(afplay_pid afplay)
}

play_af() {
	kill -19 $(afplay_pid afplay)
}
