extends Area2D

export var damage:int = 1


func _on_InimigoAtaqueArea_body_entered(body):
	body.update_health(damage)


func _on_LifeTime_timeout()-> void:
	queue_free()
