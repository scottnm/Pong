using UnityEngine;
using System.Collections;

public class PlayerSingleController : MonoBehaviour {
    Animator animator;
	// Use this for initialization
	void Start () {
	    animator = gameObject.GetComponent<Animator>();
	}
	
    void OnTriggerEnter2D(Collider2D coll) {
        animator.SetBool("Hit", true);
    }
    void OnTriggerExit2D(Collider2D coll) {
        animator.SetBool("Hit", false);
    }
}
