## Postmortem
## **Topic:** *"The Day Our Servers Decided to Go on Strike: A Postmortem of the Payment Gateway Meltdown"*
### By : Elijah Frempong
### Issue Summary

**Duration:**  

- Start: 2024-08-10, 14:30 UTC  
- End: 2024-08-10, 16:15 UTC  
- Total Duration: 1 hour, 45 minutes  

**Impact:**  
The outage affected our primary e-commerce platform, causing a complete service downtime for 60% of our users. The remaining users experienced severe latency, with page load times exceeding 30 seconds. Users were unable to complete transactions, resulting in an estimated 15% drop in daily revenue.

**Root Cause:**  
The root cause was traced to an unhandled exception in the payment gateway integration, which caused the server to enter a crash loop, leading to the service outage.

### Timeline

- **14:30 UTC:** Issue detected by monitoring alert indicating a sudden spike in server response time.
- **14:32 UTC:** Engineering team notified via Slack channel.
- **14:35 UTC:** Initial investigation began, focused on database performance, suspecting a potential query bottleneck.
- **14:50 UTC:** Assumptions shifted towards API rate limiting issues due to recent API usage spikes.
- **15:10 UTC:** Investigation revealed no anomalies in API rate limits; redirected focus to the payment gateway.
- **15:20 UTC:** Escalation to the DevOps team for deeper analysis of server logs and payment gateway interactions.
- **15:45 UTC:** DevOps identified unhandled exceptions in the payment gateway code, causing repeated server crashes.
- **15:55 UTC:** Temporary workaround deployed by disabling the payment gateway integration.
- **16:00 UTC:** Service partially restored; all users could access the platform, though without payment functionality.
- **16:15 UTC:** Permanent fix implemented by patching the payment gateway code, fully restoring the service.

### Root Cause and Resolution

The issue originated from an unhandled exception within the payment gateway's integration module. A rare edge case, triggered by a malformed API response from a third-party payment provider, caused the server to crash repeatedly. The absence of a proper error-handling mechanism led to a continuous loop of failures, resulting in a complete service outage for the majority of users.

The resolution involved two steps:

1. **Temporary Workaround:** The payment gateway integration was disabled, allowing the rest of the platform to function normally while the root cause was identified.
2. **Permanent Fix:** The payment gateway integration code was patched to handle the specific exception properly. This included adding comprehensive error logging and retry logic to prevent similar issues in the future.

### Corrective and Preventative Measures

**Improvements:**

- Improve exception handling across all external service integrations.
- Enhance monitoring to detect crash loops more quickly.
- Review and test edge cases in third-party API integrations.

**Tasks:**

1. Patch the payment gateway integration with better exception handling and retry logic.
2. Implement additional monitoring for crash loop detection and alerting.
3. Conduct a code review of all external API integrations to identify and address potential unhandled exceptions.
4. Update the incident response playbook to include specific steps for handling third-party service failures.

This postmortem aims to ensure that similar issues are prevented in the future and that our platform remains resilient to unexpected failures.
