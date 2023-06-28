extends KinematicBody2D

onready var animacao:AnimationPlayer= get_node("AnimationPlayer")
onready var textura:Sprite = get_node("Textura")	
export var move_speed:float = 256.0

var velocity:Vector2
var pode_atacar:bool = true
func  get_direction()-> Vector2:
	return Vector2(
		Input.get_axis("mover_es","mover_dir"),
		Input.get_axis("mover_up","mover_down")
	).normalized()

func _physics_process(delta:float)-> void:
	if pode_atacar==false:
		return
	move()
	animate()
	handlerAtaque()
func move()->void:
	var direction:Vector2 = get_direction()
	velocity = direction * move_speed
	move_and_slide(velocity,direction)

func animate()->void:	
	if velocity.x > 0:
		textura.flip_h = false
	if velocity.x < 0:
		textura.flip_h = true
	
	if velocity!=Vector2.ZERO:
		animacao.play("Correndo")
		return 
	animacao.play("parado")
	
func handlerAtaque()-> void:
	if Input.is_action_just_pressed("Ataque") and pode_atacar:
		pode_atacar = false
		animacao.play("Ataque")
		
		

func _on_AnimationPlayer_animation_finished(_anim_name:String)->void:
	pode_atacar = true
