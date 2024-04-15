extends CharacterBody2D

@export var move_speed: float = 256.0
@onready var animation:AnimatedSprite2D = get_node("Animated")
@onready var animacoes:AnimationPlayer = get_node("Animation")

func _physics_process(_delta:float)->void:
	if attack():
		animacoes.play("ataque")
	elif pulo():
		move()
		animate()
		
func move() -> void:
	var direcao:Vector2 = get_direction()
	velocity = direcao * move_speed
	move_and_slide()

func attack():
	if Input.is_action_pressed("ataque"):
		return true
	return false

func get_direction()->Vector2:
	return Vector2(
		Input.get_axis("move_esq","move_dir"),
		Input.get_axis("move_up","move_down")
	).normalized()

func animate()->void:
	if velocity != Vector2.ZERO:
		animation.play('run')
		animation.flip_h = true if  velocity.x < 0 else false
	else:
		animacoes.play("idle")
func pulo():
	if Input.is_action_pressed("jump"):
		var direcao:Vector2 = get_direction()
		animacoes.play("saltar")
		animation.flip_h = true if  velocity.x < 0 else false
		velocity = direcao * 100
		move_and_slide()
		return false
	return true
	
