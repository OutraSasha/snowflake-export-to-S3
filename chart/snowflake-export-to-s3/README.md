# <CHARTNAME> helm chart

## Installation

This chart assumes that `istio` and `cert-manager` are preinstalled within the cluster. It deploys a single tracking server and exposes it at `https://<CHARTNAME>.k8s.outra.co.uk`.

To install it on the cluster run

```bash
helm upgrade --install --create-namespace <CHARTNAME> ./<CHARTNAME>
```

## Parameters

| Parameter                       | Description                                                                                             | Default                                                          |
|---------------------------------|---------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `replicaCount`                  | Number of pod replicas in deployment. If HPA is enabled this value is not used                          | `1`                                                              |
| `image.repository`              | Container Image repository                                                                              | `241618103578.dkr.ecr.eu-west-1.amazonaws.com/<CHARTNAME>`       |
| `image.pullPolicy`              | Image PullPolicy                                                                                        | `ifNotPresent`                                                   |
| `image.tag`                     | Docker Container image tag                                                                              | `Chart.AppVersion`                                               |
| `imagePullSecrets`              | Specify docker-registry secret names as an array                                                        | `[]` (does not add image pull secrets to deployed pods)          |
| `nameOverride`                  | String to partially override fullname template                                                          | `nil`                                                            |
| `fullnameOverride`              | String to fully override fullname template                                                              | `nil`                                                            |
| `namespace.create`              | Create  Namespace                                                                                       | `true`                                                           |
| `serviceAccount.create`         | Create serviceAccount for the pods                                                                      | `true`                                                           |
| `serviceAccount.annotation`     | Created service acount annotations                                                                      | `[]`                                                             |
| `serviceAccount.name`           | Name of service acount                                                                                  | `nil`                                                            |
| `podAnnotations`                | Annotations for pods                                                                                    | `{}` (evaluated as a template)                                   |
| `podSecurityContext.fsGroup`    | pods' Security Context fsgroup                                                                          | `65534`                                                          |
| `securityContext`               | Containers' Security Context                                                                            | `{}`                                                             |
| `command`                       | Entrypoint array. The docker image's ENTRYPOINT is used if this is not provided.                        | `nil`                                                            |
| `args`                          |      Arguments to the entrypoint. The docker image's CMD is used if this is not provided.               | `nil`                                                            |
| `gateway.enabled`               | Enable Gateway and VirtualService resource                                                              | `false`                                                          |
| `gateway.hosts`                 | Array of hosts for Gateway and VirtualService                                                           | `["<CHARTNAME>.k8s.outra.co.uk"]`                                |
| `cert.enabled`                  | Create ertificate object                                                                                | `false`                                                          |
| `cert.commonName`               | Common Name value of certificate                                                                        | `<CHARTNAME>.k8s.outra.co.uk`                                    |
| `tls.mode`                      | Istio IngressGateway TLS mode (`PASSTHROUGH`, `SIMPLE`, `MUTUAL`)                                       | `SIMPLE`                                                         |
| `overallTimeout`                | The "top-level" timeout enforced when clients call your service. This timeout is inclusive of retries.  | `30s`                                                            |
| `retries.*`                     | Istio configuration for client retry policy. See Istio retry documentation for values.                  | Check `values.yaml`  file                                        |
| `resources.limits`              | The resources limits for the container                                                                  | Check `values.yaml` file                                         |
| `resources.requests`            | The requested resources for the container                                                               | Check `values.yaml` file                                         |
| `livenessProbe`                 | Liveness probe configuration                                                                            | Check `values.yaml` file                                         |
| `readinessProbe`                | Readiness probe configuration                                                                           | Check `values.yaml` file                                         |
| `configmap.mountPath`           | The directory inside your pod to mount the config map                                                   | `/config/<CHARTNAME>-config`                                     |
| `configmap.fileName`           |  The file name of the config map, when mounted in the pod.                                               | `/config/<CHARTNAME>-config`                                     |
| `configmap.content`           |  YAML keys and values under content are copied verbatim into the configmap's content.                     | `{}`                                                             |

## AWS IAM Service account annotation

If you would like the pod to access AWS resources you need to attach a role to a service account.

You need to create a service account with the `eksctl`. After creation, you should set values in `values.yaml` to

```yaml
serviceAccount:
  create: false
  name: <SERVICE_ACCOUNT_NAME>
podSecurityContext:
  fsGroup: 65534
```
