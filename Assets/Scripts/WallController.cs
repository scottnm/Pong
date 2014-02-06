using UnityEngine;
using System.Collections;

public class WallController : MonoBehaviour {
    Animator animator;

	// Use this for initialization
	void Start () {
	    animator = gameObject.GetComponent<Animator>();
	}
	
    void OnTriggerEnter2D(Collider2D coll) {
        Debug.Log("I was hit.");
        animator.SetBool("Hit", true);
    }
    void OnTriggerExit2D(Collider2D coll) {
        Debug.Log("it left");
        animator.SetBool("Hit", false);
    }
}
