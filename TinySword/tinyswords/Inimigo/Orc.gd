extends KinematicBody2D

onready var animacao:AnimationPlayer = get_node("Animation")
onready var textura:Sprite = get_node("Textura")	
onready var aux_animation:AnimationPlayer = get_node("Aux_Animation")


var velocity:Vector2
export var speed:float = 190
export var damage:int = 1
export var health:int = 3
export var limite_dist:float =60.0 
var pode_morrer =false
var pode_atacar:bool = true
var player:KinematicBody2D = null



func handler_ataque()->void:
	pass


func animate()->void:
	if velocity.x > 0 :
		textura.flip_h= false
	if velocity.x < 0 :	
		textura.flip_h= true
	if velocity!=Vector2.ZERO:
		animacao.play("Correndo")
		return
	
	animacao.play("Parado")


func _physics_process(delta:float)-> void:
	if pode_morrer == true:
		return
	if player == null:
		velocity = Vector2.ZERO
		animate()
		return

	var direction:Vector2 = global_position.direction_to(player.global_position)
	var distancia:float = global_position.distance_to(player.global_position)
	
	if distancia < limite_dist:
		animacao.play("Ataque")
		return
	
	velocity = direction* speed
	
	move_and_slide(velocity,direction)
	animate()

func update_health(value:int)->void:
	health-=value
	if health < 0:
		pode_morrer = true
		animacao.play("Morreu")
		return 
	aux_animation.play("dano")


func _on_DetectionArea_body_entered(body):
	player = body
	
func _on_DetectionArea_body_exited(body):
	player = null
