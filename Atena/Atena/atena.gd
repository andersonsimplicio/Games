extends CharacterBody2D

@export var move_speed = 256.0
@onready var animacoes:AnimationPlayer = get_node("AnimationPlayer")
 
func _physics_process(_delta:float)->void:
	animate()

func animate()->void:
	if velocity != Vector2.ZERO:
		pass	
	else:
		animacoes.play("idle")
	

func get_direction()->Vector2:
	return Vector2(
		Input.get_axis("move_esq","move_dir"),
		Input.get_axis("move_esq","move_dir")
	).normalized()
