using UnityEngine;
using System.Collections;

public class BallController : MonoBehaviour {
	
	private float speed = 6.0f;
	
	private Vector2 velocity;
	
	void Start() {
		Reset(PlayerController.Player.Player1);
	}
	
	void FixedUpdate() {
		speed += 0.1f * Time.fixedDeltaTime;
		
		velocity.Normalize();
		velocity *= speed;
		
		rigidbody2D.velocity = velocity;
	}
	
	void OnTriggerEnter2D(Collider2D other) {
		if(other.tag == "Player1" || other.tag == "Player2") {
			HandlePlayerCollision(other);
		} else if(other.tag == "Wall") {
			HandleWallCollision(other);
		}
	}
	
	void HandlePlayerCollision(Collider2D other) {
		velocity.x *= -1;
	}
	
	void HandleWallCollision(Collider2D other) {
		velocity.y *= -1;
	}
	
	public void Reset(PlayerController.Player player) {
		speed = 6.0f;
		int direction = -1;
		if(player == PlayerController.Player.Player2) {
			direction = 1;
		}
		
		transform.position = new Vector3(0,0,0);
		velocity = new Vector2(speed * direction, Random.Range(2f,speed));
	}
}
