using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class EventManager : MonoBehaviour
{
    public static event Action ExampleEvent;

    public static event Action TestEvent;

    private void Update()
    {
        if (Input.GetMouseButtonDown(0))
        {
            if (ExampleEvent != null)
                ExampleEvent();
            ExampleEvent?.Invoke();
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            if (TestEvent != null)
                TestEvent();
            TestEvent?.Invoke();
        }
    }
}
